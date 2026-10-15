@echo off
title GuardianWare AI // Safety & Compliance Command Center
color 0B
cls
echo ===============================================================================
echo                GUARDIANWARE AI // WAREHOUSE SAFETY COMMAND CENTER             
echo                       ENTERPRISE MISSION CONTROL v2.4                         
echo ===============================================================================
echo.
echo [*] Initializing Autonomous EHS Telemetry Server...
echo [*] Host: http://127.0.0.1:8000
echo [*] OpenAPI Docs: http://127.0.0.1:8000/docs
echo [*] Press CTRL+C to terminate the server.
echo.
python app.py
pause
