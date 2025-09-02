# CyberSecurity Tutor AI

An AI-powered virtual teaching assistant for cybersecurity education using scaffolding techniques.

## Quick Start

### 1. Setup
- Install Python 3.8+ and Node.js 14+
- Create `keys.env` file with your OpenAI API key:
  ```
  OPENAI_API_KEY=your_api_key_here
  SECRET_KEY=random_secret_key_here
  ```

### 2. Install Dependencies
```bash
# Create the venv environment
python -m venv venv

# Enter the venv environment
venv\Scripts\activate

# Then inside the venv environment install the dependencies
pip install -r requirements.txt

# Exit venv and install frontend dependencies
cd frontend
npm install
cd ..
```

### 3. Add Students
```bash
python add_users.py
```
Enter students in format: `student_id    password`, with a tab between the two variables

### 4. Start Application
Double-click `start_servers.bat` or run:
```bash
start_servers.bat
```

### 5. Access
- Frontend: http://localhost:5173
- Backend: http://localhost:8000

## Features

- **AI-Powered Scaffolding**: Step-by-step guidance without direct answers
- **User Management**: Secure login with KCL student IDs
- **Course Integration**: Upload PDF course materials for context
- **Comprehensive Logging**: Track learning journeys and research data
- **Easy Customization**: Modify scaffolding logic by editing prompt files

## File Structure

```
Project/
├── chatbot/          # Backend application
├── frontend/         # React web interface
├── prompt/           # Scaffolding prompt files
├── log/              # Login and token logs
├── chat_history/     # Individual conversation logs
├── PDF/              # Course materials
├── add_users.py      # Add student accounts
├── change_password.py # Admin password management
└── start_servers.bat # Launch application
```

## Admin Tools

- **Add Students**: `python add_users.py`
- **Change Password**: `python change_password.py`
- **Backup Database**: `python backup_and_wipe_db.py`

## Research Features

- Individual conversation logs in `chat_history/`
- Login activity in `log/login_log.txt`
- Token usage tracking in `log/token_log.txt`
- Easy prompt modification for different scaffolding approaches

## Tech Stack

- **Backend**: Django, OpenAI API, SQLite
- **Frontend**: React, Vite, TailwindCSS
- **AI**: GPT-4o-mini with Files API integration 
