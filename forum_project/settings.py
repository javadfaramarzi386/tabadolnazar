

# SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-dzh0^t5i#)cvq^u-gb^1to@8bp+ygt8l(b1w^stti%(o&wded1')


"""
Django settings for forum_project project.
"""

import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ========================================
# تنظیمات امنیتی و توسعه
# ========================================

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-dzh0^t5i#)cvq^u-gb^1to@8bp+ygt8l(b1w^stti%(o&wded1')

# اصلاح شد: خواندن خودکار از محیط یا قرار دادن روی False واقعی (بولین)
# اگر در پلتفرم‌هایی مثل Render یا لیارا هستید، خودش متغیر محیطی را می‌خواند
# DEBUG = os.getenv("DEBUG", "False") == "True"

# اگر می‌خواهید کاملاً اجباری False باشد، خط زیر را از کامنت خارج کنید:


DEBUG = False

ALLOWED_HOSTS = ['.railway.app', '127.0.0.1', 'localhost']

# ========================================
# اپلیکیشن‌ها
# ========================================
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',  # باید اول باشد
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # اپ‌های پروژه شما
    'accounts',
    'forum',
    'django_extensions',
]

# ========================================
# Middleware
# ========================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'forum_project.urls'
WSGI_APPLICATION = 'forum_project.wsgi.application'

# ========================================
# Templates
# ========================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ========================================
# دیتابیس
# ========================================
if os.getenv('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ========================================
# Static & Media Files
# ========================================
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ========================================
# بقیه تنظیمات
# ========================================
LANGUAGE_CODE = 'fa-ir'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True

LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# امنیت (در Railway)
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # SECURE_SSL_REDIRECT = True   # فعلاً کامنت بماند