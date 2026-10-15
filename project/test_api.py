import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.seed_data import seed_database

client = TestClient(app)

@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    seed_database()

def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "HEALTHY"
    assert "version" in data

def test_observability_metrics():
    response = client.get("/api/observability/metrics")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ONLINE"
    assert "inference_latency_ms" in data

def test_get_warehouses():
    response = client.get("/api/warehouses")
    assert response.status_code == 200
    warehouses = response.json()
    assert len(warehouses) >= 4
    assert any(w["id"] == "WH-CHI-01" for w in warehouses)

def test_get_warehouse_zones():
    response = client.get("/api/warehouses/WH-CHI-01/zones")
    assert response.status_code == 200
    zones = response.json()
    assert len(zones) >= 6
    for z in zones:
        assert "risk_score" in z
        assert "explainability" in z

def test_get_cameras():
    response = client.get("/api/cameras?warehouse_id=WH-CHI-01")
    assert response.status_code == 200
    cameras = response.json()
    assert len(cameras) >= 4

def test_toggle_camera_detector():
    response = client.patch("/api/cameras/CAM-01/detectors", json={"ppe_detector": False})
    assert response.status_code == 200
    assert response.json()["ppe_detector"] is False
    # Reset back
    client.patch("/api/cameras/CAM-01/detectors", json={"ppe_detector": True})

def test_incidents_lifecycle():
    # 1. Get incidents
    res = client.get("/api/incidents")
    assert res.status_code == 200
    incidents = res.json()
    assert len(incidents) >= 4

    # 2. Create an incident
    create_res = client.post("/api/incidents", json={
        "warehouse_id": "WH-CHI-01",
        "zone_id": "ZONE-DOCK",
        "camera_id": "CAM-01",
        "incident_type": "FORKLIFT_SPEED",
        "severity": "HIGH",
        "description": "Forklift FL-02 clocked at 18.5 km/h in 8 km/h pedestrian cross-aisle.",
        "confidence": 0.97
    })
    assert create_res.status_code == 200
    created = create_res.json()
    inc_id = created["id"]
    assert created["incident_type"] == "FORKLIFT_SPEED"
    assert "root_cause_analysis" in created

    # 3. Acknowledge
    ack_res = client.post(f"/api/incidents/{inc_id}/acknowledge")
    assert ack_res.status_code == 200
    assert ack_res.json()["status"] == "INVESTIGATING"

    # 4. Resolve
    resolve_res = client.patch(f"/api/incidents/{inc_id}", json={"status": "RESOLVED"})
    assert resolve_res.status_code == 200
    assert resolve_res.json()["status"] == "RESOLVED"

def test_capa_workflow():
    # Create CAPA
    capa_res = client.post("/api/capa", json={
        "incident_id": "INC-2026-0891",
        "title": "Calibrate Forklift LiDAR Governor",
        "description": "Set vehicle speed limiter to 6 km/h cap.",
        "owner_name": "Dave Reynolds",
        "priority": "HIGH",
        "due_date": "2026-09-20T12:00:00Z"
    })
    assert capa_res.status_code == 200
    capa = capa_res.json()
    capa_id = capa["id"]

    # Escalate
    esc_res = client.post(f"/api/capa/{capa_id}/escalate")
    assert esc_res.status_code == 200
    assert esc_res.json()["status"] == "ESCALATED"
    assert esc_res.json()["escalation_level"] == 1

def test_compliance_audit_and_pdf_generation():
    audit_res = client.post("/api/audits/generate", json={
        "warehouse_id": "WH-CHI-01",
        "standard_id": "OSHA-1910.132",
        "audit_period": "Last 30 Days"
    })
    assert audit_res.status_code == 200
    data = audit_res.json()
    assert "score" in data
    assert "pdf_url" in data
    assert data["pdf_url"].endswith(".pdf")

def test_checklists_and_tag_audits():
    # Submit checklist
    chk_res = client.post("/api/checklists", json={
        "warehouse_id": "WH-CHI-01",
        "checklist_type": "FORKLIFT_PRE_SHIFT",
        "asset_id": "ASSET-FL-09",
        "inspector_name": "Carlos Martinez",
        "items_data": [
            {"title": "Brakes", "passed": True},
            {"title": "Horn", "passed": True}
        ]
    })
    assert chk_res.status_code == 200
    assert chk_res.json()["score"] == 100.0

    # Scan tag audit
    tag_res = client.post("/api/checklists/tag-audits", json={
        "warehouse_id": "WH-CHI-01",
        "tag_type": "NFC",
        "tag_code": "NFC-FL-09",
        "asset_or_loc_name": "Toyota Forklift FL-09",
        "scanned_by": "Carlos Martinez",
        "condition_status": "OPTIMAL"
    })
    assert tag_res.status_code == 200
    assert tag_res.json()["tag_code"] == "NFC-FL-09"

def test_simulation_trigger():
    sim_res = client.post("/api/simulation/trigger-event", json={
        "warehouse_id": "WH-CHI-01",
        "incident_type": "SMOKE_FIRE",
        "severity": "CRITICAL"
    })
    assert sim_res.status_code == 200
    assert sim_res.json()["incident_type"] == "SMOKE_FIRE"
    assert sim_res.json()["severity"] == "CRITICAL"

def test_spa_frontend_serving():
    res = client.get("/")
    assert res.status_code == 200
    assert "GuardianWare AI" in res.text

    res_css = client.get("/css/style.css")
    assert res_css.status_code == 200
    assert "--cyan-primary" in res_css.text

    res_js = client.get("/js/app.js")
    assert res_js.status_code == 200
    assert "GuardianWareApp" in res_js.text
