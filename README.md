# CyberSecurity Tutor AI

An interactive AI-powered chatbot that helps users learn about cybersecurity concepts, best practices, and specific topics.

## Project Structure

```
Project/
├── backend/          # Django backend server
├── frontend/         # React frontend application
├── manage.py         # Django management script
├── requirements.txt  # Python dependencies
└── start_servers.bat # Batch script to start both servers
```

## Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- npm (Node Package Manager)
- Windows OS

## Setup

1. Set up the Python virtual environment and install dependencies:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   cd ..
   ```

3. Configure environment variables:
   - Create a `keys.env` file in the root directory
   - Add your API keys and other configuration

## Running the Application

### Method 1: Using the Batch File
Simply double-click the `start_servers.bat` file or run it from the command line:
```bash
start_servers.bat
```

### Method 2: Manual Start
1. Start the Django backend server:
   ```bash
   python manage.py runserver
   ```

2. In a new terminal, start the React frontend:
   ```bash
   cd frontend
   npm run dev
   ```

## Accessing the Application

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000

## Features

- Interactive chat interface
- Real-time responses
- Cybersecurity-focused conversations
- Modern and responsive UI

## Tech Stack

- Frontend:
  - React
  - Vite
  - TailwindCSS
  
- Backend:
  - Django
  - Django REST Framework
  - OpenAI API 