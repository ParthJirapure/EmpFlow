import sys
import os
import time
import webbrowser
import threading
import uvicorn

def open_browser():
    """Wait briefly for server initialization, then open browser."""
    time.sleep(1.2)
    webbrowser.open("http://127.0.0.1:8000")

if __name__ == "__main__":
    # Ensure project root is in sys.path
    project_root = os.path.dirname(os.path.abspath(__file__))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    print("\n" + "=" * 70)
    print("   GUARDIANWARE AI // WAREHOUSE SAFETY COMMAND CENTER")
    print("=" * 70)
    print("  [*] Server URL:   http://127.0.0.1:8000  (Ctrl + Click to open)")
    print("  [*] OpenAPI Docs: http://127.0.0.1:8000/docs")
    print("  [*] Press CTRL+C to terminate.")
    print("=" * 70 + "\n")

    # Prevent multiple browser tabs opening if uvicorn reloads
    if not os.environ.get("APP_BROWSER_OPENED"):
        os.environ["APP_BROWSER_OPENED"] = "true"
        threading.Thread(target=open_browser, daemon=True).start()

    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
