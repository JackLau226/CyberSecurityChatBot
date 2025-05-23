@echo off
echo Starting CyberSecurity Tutor AI servers...

:: Wait for 5 seconds to ensure choice
timeout /t 5 /nobreak
echo.
echo Servers are starting...
echo.
echo Starting Django backend server... 

:: Start Django backend server
start cmd /k "echo Starting Django backend server... && venv\Scripts\activate && python manage.py runserver"

:: Wait for 5 seconds to ensure backend starts first
timeout /t 5 /nobreak
echo.
echo Starting React frontend...
echo.

:: Start React frontend
start cmd /k "echo Starting React frontend... && cd frontend && npm run dev"


echo Frontend will be available at: http://localhost:5173
echo Backend will be available at: http://localhost:8000
echo.
echo Press any key to close this window (servers will continue running)
pause > nul 