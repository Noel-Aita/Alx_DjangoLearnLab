# LibraryProject/settings.py
import os
from pathlib import Path

from users.models import CustomUser


BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY
DEBUG = False # Ensure False in production


ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']


# Use the custom user model
AUTH_USER_MODEL = 'bookshelf.CustomUser'




# Cookies & HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True


# HSTS
SECURE_HSTS_SECONDS = 31536000 # 1 year; adjust for staging
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


# Clickjacking & content sniffing
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True


# Content Security Policy (CSP) - recommended: install django-csp
# pip install django-csp
MIDDLEWARE = [
'django.middleware.security.SecurityMiddleware',
# If you use django-csp, add it here
# 'csp.middleware.CSPMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.common.CommonMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Example CSP settings (if django-csp is used):
# CSP_DEFAULT_SRC = ("'self'",)
# CSP_SCRIPT_SRC = ("'self'", 'cdnjs.cloudflare.com')
# CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com')


# Media files (for profile_photo)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')