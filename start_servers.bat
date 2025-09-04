@echo off
echo Starting CyberSecurity Tutor AI servers...

:: Wait 5 seconds
timeout /t 5 /nobreak
echo.
echo Servers are starting...
echo.
echo Starting Django backend server... 

:: Start Django (bind all interfaces)
start cmd /k "echo Starting Django backend server... && venv\Scripts\activate && py manage.py runserver 0.0.0.0:8000"

:: Wait 5 seconds
timeout /t 5 /nobreak
echo.
echo Starting React frontend...
echo.

:: Start React 
start cmd /k "echo Starting React frontend... && cd frontend && npm run dev -- --host 0.0.0.0 --port 5173"


echo Frontend will be available at: http://localhost:5173
echo You can check if backend is running at: http://localhost:8000
echo.
echo Press any key to close this window (servers will continue running)
pause > nul 