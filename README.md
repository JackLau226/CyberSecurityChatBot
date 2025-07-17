# CyberSecurity Tutor AI

An interactive AI-powered chatbot that helps users learn about cybersecurity concepts, best practices, and specific topics.

## Project Structure

```
Project/
├── chat_history      # Chat history of students
├── backend/          # Django backend server
├── debug/            # Debug scripts
├── frontend/         # React frontend application
├── log/              # Log files for login and tokens usage
├── prompt/           # Different prompt files
├── requirements.txt  # Python dependencies
├── manage.py         # Django management script
├── add_users.py      # Python script for adding users
├── backup_and_wipe_db.py # Python script for backup and wipe database
├── change_password.py    # Python script for changing password of one student
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

4. Set up the database and create users:
   ```bash
   python add_users.py
   ```

(Optional)
.. Add test users into the database
   ```bash
   python add_test_users.py
   ```

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

- **User Authentication**: Multi-user login system with database-backed user accounts
- Interactive chat interface
- Real-time responses
- Cybersecurity-focused conversations
- Modern and responsive UI
- **Comprehensive Logging System**:
  - Conversation logs per user in `chat_history/` folder
  - Login activity logs in `log/login_log.txt`
  - Token usage logs in `log/token_log.txt`

## Test Users

After setting up the database, you can use these test credentials:

- Username: `admin`, Password: `admin123`
- Username: `user1`, Password: `password1`
- Username: `user2`, Password: `password2`
- Username: `test`, Password: `test123`
- Username: `demo`, Password: `demo123`

## Logging System

The application includes a comprehensive logging system:

### Login Log (`log/login_log.txt`)
- Records all successful user logins
- Format: `YYYY-MM-DD HH:MM:SS - User {username} logged in successfully.`

### Token Log (`log/token_log.txt`)
- Records all chat messages with token counts
- Format: `YYYY-MM-DD HH:MM:SS - User {username} sent message: '{message}' (Token count: {count})`
- Messages longer than 100 characters are truncated in the log

### Conversation Logs (`chat_history/{username}.txt`)
- Individual conversation logs for each user
- Records both user messages and AI responses
- Format: `YYYY-MM-DD HH:MM:SS - {sender}: {message}`

## Tech Stack

- Frontend:
  - React
  - Vite
  - TailwindCSS
  
- Backend:
  - Django
  - Django REST Framework
  - OpenAI API
  - SQLite Database 