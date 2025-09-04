from pathlib import Path
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv('keys.env')

# Load centralized app config (JSON at project root)
BASE_DIR = Path(__file__).resolve().parent.parent
APP_CONFIG_PATH = BASE_DIR / 'app_config.json'
try:
    with open(APP_CONFIG_PATH, 'r', encoding='utf-8') as f:
        APP_CONFIG = json.load(f)
except Exception:
    APP_CONFIG = {
        'EXTERNAL_DDNS': 'jackcityone.asuscomm.com',
        'EXTERNAL_IP': '113.253.163.143',
        'DJANGO_PORT': 8000,
        'REACT_PORT': 5173,
    }

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# (BASE_DIR already defined above to load app_config)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    APP_CONFIG.get('EXTERNAL_IP', ''),
    APP_CONFIG.get('EXTERNAL_DDNS', ''),
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chatbot',  # our chatbot app
    'corsheaders',  # CORS support
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # CORS middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS settings (not strictly needed when using Vite proxy, but kept for clarity)
CORS_ALLOWED_ORIGINS = [
    f"http://localhost:{APP_CONFIG.get('REACT_PORT', 5173)}",
    f"http://127.0.0.1:{APP_CONFIG.get('REACT_PORT', 5173)}",
    f"http://{APP_CONFIG.get('EXTERNAL_IP', '')}:{APP_CONFIG.get('REACT_PORT', 5173)}",
    f"http://{APP_CONFIG.get('EXTERNAL_DDNS', '')}:{APP_CONFIG.get('REACT_PORT', 5173)}",
]

CORS_ALLOW_CREDENTIALS = True
