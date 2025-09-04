from pathlib import Path
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv('keys.env')

# (No Python module import for config; we load centralized JSON below)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
APP_CONFIG_PATH = BASE_DIR / 'app_config.json'
try:
    with open(APP_CONFIG_PATH, 'r', encoding='utf-8') as f:
        APP_CONFIG = json.load(f)
except Exception:
    # Safe defaults with no hard-coded external hostnames/IPs
    APP_CONFIG = {
        'EXTERNAL_DDNS': '',
        'EXTERNAL_IP': '',
        'DJANGO_PORT': 8000,
        'REACT_PORT': 5173,
    }

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [h for h in [
    'localhost',
    '127.0.0.1',
    APP_CONFIG.get('EXTERNAL_IP', ''),
    APP_CONFIG.get('EXTERNAL_DDNS', ''),
] if h]


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
CORS_ALLOWED_ORIGINS = [o for o in [
    f"http://localhost:{APP_CONFIG.get('REACT_PORT', 5173)}",
    f"http://127.0.0.1:{APP_CONFIG.get('REACT_PORT', 5173)}",
    f"http://{APP_CONFIG.get('EXTERNAL_IP', '')}:{APP_CONFIG.get('REACT_PORT', 5173)}" if APP_CONFIG.get('EXTERNAL_IP') else '',
    f"http://{APP_CONFIG.get('EXTERNAL_DDNS', '')}:{APP_CONFIG.get('REACT_PORT', 5173)}" if APP_CONFIG.get('EXTERNAL_DDNS') else '',
] if o]

CORS_ALLOW_CREDENTIALS = True

# URLs and templates
ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
