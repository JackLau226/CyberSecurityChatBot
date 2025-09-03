#!/bin/bash

echo "Starting CyberSecurity Tutor AI servers..."
echo "=========================================="

# Function to cleanup background processes on exit
cleanup() {
    echo ""
    echo "Stopping servers..."
    if [ ! -z "$DJANGO_PID" ]; then
        kill $DJANGO_PID 2>/dev/null
        echo "✓ Django server stopped"
    fi
    if [ ! -z "$FRONTEND_PID" ]; then
        kill $FRONTEND_PID 2>/dev/null
        echo "✓ React frontend stopped"
    fi
    echo "All servers stopped. Goodbye!"
    exit 0
}

# Set trap to cleanup on script exit
trap cleanup INT TERM EXIT

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please create it first with: python3 -m venv venv"
    exit 1
fi

# Check if requirements are installed
if [ ! -f "venv/bin/python" ]; then
    echo "❌ Virtual environment not properly set up!"
    echo "Please activate and install requirements:"
    echo "  source venv/bin/activate"
    echo "  pip install -r requirements.txt"
    exit 1
fi

# Check if frontend dependencies are installed
if [ ! -d "frontend/node_modules" ]; then
    echo "⚠️  Frontend dependencies not found!"
    echo "Installing frontend dependencies..."
    cd frontend
    npm install
    cd ..
    echo "✓ Frontend dependencies installed"
fi

echo ""
echo "Starting Django backend server..."

# Activate virtual environment and start Django
source venv/bin/activate
python manage.py runserver &
DJANGO_PID=$!

# Wait a moment for Django to start
sleep 3

# Check if Django started successfully
if kill -0 $DJANGO_PID 2>/dev/null; then
    echo "✓ Django backend server started (PID: $DJANGO_PID)"
    echo "  Backend available at: http://localhost:8000"
else
    echo "❌ Failed to start Django server"
    exit 1
fi

echo ""
echo "Starting React frontend..."

# Start React frontend
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

# Wait a moment for React to start
sleep 3

# Check if React started successfully
if kill -0 $FRONTEND_PID 2>/dev/null; then
    echo "✓ React frontend started (PID: $FRONTEND_PID)"
    echo "  Frontend available at: http://localhost:5173"
else
    echo "❌ Failed to start React frontend"
    cleanup
    exit 1
fi

echo ""
echo "🎉 All servers are running successfully!"
echo "=========================================="
echo "Frontend: http://localhost:5173"
echo "Backend:  http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop all servers"
echo ""

# Wait for user to stop
wait
