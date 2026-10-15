# GuardianWare AI // Safety & Compliance Command Center for Warehousing

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg?style=flat&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.13+-3776AB.svg?style=flat&logo=python)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?style=flat&logo=docker)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-Enterprise-blue.svg)](#)

GuardianWare AI is a production-grade, enterprise-level Safety & Compliance Command Center engineered for high-velocity warehousing, distribution centers, and fulfillment hubs. The system unifies real-time computer vision surveillance, autonomous OSHA & ISO 45001 regulatory auditing, dynamic warehouse digital twin floor mapping, incident & CAPA lifecycle management, physical QR/NFC asset audits, and machine-learning hazard risk forecasting into a high-performance, cinematic mission control center.

---

## System Architecture

```
                                  +---------------------------------------+
                                  |  Cinematic Command Center (Frontend)  |
                                  |   Canvas 2D Digital Twin & CCTV HUD   |
                                  +-------------------+-------------------+
                                                      |
                                     HTTP REST & WebSockets (/ws/alerts)
                                                      |
                                  +-------------------v-------------------+
                                  |        FastAPI Enterprise Core        |
                                  |  Async ASGI Engine & Telemetry Hub    |
                                  +---------+--------+---------+----------+
                                            |        |         |
              +-----------------------------+        |         +---------------------------+
              |                                      |                                     |
+-------------v--------------+    +------------------v---------------+    +----------------v---------------+
|    Computer Vision HUD     |    |   OSHA / ISO 45001 Auditor       |    |  Predictive Risk & XAI Engine  |
| 10 Real-Time CV Detectors  |    | Scored Clauses & PDF Reports     |    | SHAP Attribution & Forecasting |
+----------------------------+    +----------------------------------+    +--------------------------------+
              |                                      |                                     |
              +-----------------------------+        |         +---------------------------+
                                            |        |         |
                                  +---------v--------v---------v----------+
                                  |     SQLAlchemy 2.0 Dual Engine        |
                                  |   SQLite (Local) / PostgreSQL (Prod)  |
                                  +---------------------------------------+
```

---

## Key Capabilities & Detection Modules

### 1. Real-Time Computer Vision Monitoring (10 Detection Modules)
1. **PPE Detection**: Real-time detection of mandatory hardhats, high-visibility vests, protective gloves, steel-toe boots, and eyewear.
2. **Restricted-Zone Intrusion**: Virtual tripwires and exclusion polygons around automated palletizers, robotic sorters, and high-voltage bays.
3. **Unsafe Forklift Behavior**: Speed tracking (>10 km/h in pedestrian aisles), erratic steering, mast elevated during transit, phone distraction.
4. **Worker-Forklift Proximity**: Dynamic proximity bounding circles with critical alerts triggered when vehicle-pedestrian clearance drops below 3.0 meters.
5. **Slip / Trip / Fall Detection**: Rapid vertical velocity drop and posture analysis with prolonged immobility timers.
6. **Smoke & Fire Detection**: Optical smoke opacity analysis and thermal hazard contour recognition.
7. **Spills & Liquid Hazards**: Specular reflection and expanding puddle detection for hazardous chemical and hydraulic oil leaks.
8. **Blocked Emergency Exits**: Static obstruction detection in designated yellow diagonal hatched egress zones and fire doors.
9. **Overcrowding Detection**: Zone personnel density tracking against maximum safety capacity thresholds.
10. **Unsafe Stacking Detection**: Pallet stack lateral deflection analysis (>5° tilt limit), uneven overhangs, and tier height limit exceedance.

### 2. Intelligent Risk Scoring & Explainable AI (XAI)
- **Dynamic Zone Risk Index (0-100)**: Real-time risk scoring computed from violation frequency, hazard severity weights, proximity exposure time, and ambient factors.
- **SHAP-Style Feature Attribution**: Visual breakdown of exact points and percentages contributed by each hazard category (e.g. *Vehicle Proximity: +34 pts*, *PPE Non-Compliance: +22 pts*, *Blocked Egress: +18 pts*).

### 3. Automated OSHA / ISO 45001 Compliance Audits
- Integrated regulatory frameworks:
  - **OSHA 1910.132**: General PPE requirements
  - **OSHA 1910.178**: Powered Industrial Trucks (Forklifts)
  - **OSHA 1910.36 / 37**: Exit routes and egress maintenance
  - **OSHA 1910.176**: Material handling and safe pallet stacking
  - **ISO 45001:2018**: Occupational Health & Safety Management System clauses
- Autonomous audit generation producing scored compliance certificates, gap analysis, and one-click downloadable ReportLab PDFs.

### 4. Interactive Digital Twin 2D Floor Map
- Canvas-based floorplan of warehouse facilities (Dock Doors 1-6, High-Bay Aisles A1-B4, Cold Storage, Staging, Hazard Room).
- Live heatmaps: Violation frequency, worker density, animated forklift guide-path routes, and real-time pulsing alert beacons.
- Clickable zones showing real-time occupancy, active camera links, and open hazard telemetry.

### 5. Incident & CAPA Lifecycle Management
- Full incident lifecycle: `Open` ➔ `Investigating` ➔ `CAPA Assigned` ➔ `Resolved` ➔ `Escalated`.
- Automated Root-Cause Analysis (RCA): 5-Whys generation and Ishikawa (Fishbone) diagram mapping.
- Corrective & Preventive Action (CAPA) Kanban board with assignees, due dates, automated SLA escalation, and verification sign-offs.

### 6. Digital Inspection Checklists & QR / NFC Audits
- Pre-shift forklift safety inspection checklist (brakes, horn, tires, hydraulics, beacon, seatbelt).
- Daily perimeter and fire safety walkthrough checklist.
- Mobile QR / NFC asset and location scanner simulator to audit tags on racks (`QR-RACK-A04`), forklifts (`NFC-FL-04`), and fire extinguishers (`QR-EXT-12`).

### 7. Multi-Warehouse Support & RBAC
- Multi-facility switching:
  - **Chicago Mega-Hub (WH-CHI-01)**
  - **Rotterdam Euro-Port (WH-ROT-02)**
  - **Dallas Distribution (WH-DFW-03)**
  - **Singapore Gateway (WH-SIN-04)**
- 5 Enterprise Roles with instantaneous header persona switcher:
  1. `SUPER_ADMIN` (Global EHS VP)
  2. `SAFETY_MANAGER` (Lead Warehouse Safety Officer)
  3. `AUDITOR` (OSHA/ISO Certified Lead)
  4. `FLOOR_SUPERVISOR` (Dock & Staging Team Lead)
  5. `WORKER` (Forklift Operator)

---

## Quickstart Guide (Zero Setup)

The application runs out of the box with embedded SQLite and synthetic live camera streams.

### Prerequisites
- Python 3.11+ installed

### 1. Clone & Install Dependencies
```bash
git clone <repository_url>
cd AIML
python -m pip install -r requirements.txt
```

### 2. Launch Command Center
```bash
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
```

### 3. Open in Browser
Navigate to:
```
http://127.0.0.1:8000
```

- Swagger OpenAPI Documentation: `http://127.0.0.1:8000/docs`
- Health Check: `http://127.0.0.1:8000/api/health`

---

## Production Docker Deployment

Deploy with high-availability PostgreSQL using Docker Compose:

```bash
docker compose up --build -d
```

Check service status:
```bash
docker compose ps
docker compose logs -f app
```

---

## Automated Test Suite

Run the full end-to-end automated test suite verifying all REST endpoints, risk scoring, OSHA audits, PDF generation, and frontend serving:

```bash
python -m pytest -v tests/test_api.py
```

---

## Live Demo & Simulation Lab

Use the **SIMULATION LAB** button in the header to inject live synthetic violations into the real-time pipeline:
- `🚨 Forklift Proximity Breach (1.2m)`
- `🔥 Battery Bay Smoke / Fire Plume`
- `⚠️ Worker Down / Slip & Fall`
- `🚪 Blocked Fire Exit Door E-03`
- `👷 Missing Hardhat at Dock Bay 2`
- `📦 Pallet Stack 8.4° Tilt Danger`
- `🧪 Hazmat Chemical Spill Puddle`
- `👥 Zone Overcrowding (110%)`

Observe instantaneous audible alerts (Web Audio API), glowing HUD updates, real-time WebSocket broadcast, and digital twin heatmap shifts.
