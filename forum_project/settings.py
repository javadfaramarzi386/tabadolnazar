# forum_project/settings.py

import os
import sys
from pathlib import Path

from dotenv import load_dotenv


# =========================================================
# Base Directory
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================
# Environment
# =========================================================

load_dotenv(BASE_DIR / ".env")


# =========================================================
# Security
# =========================================================

SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY is not configured.")


# =========================================================
# Debug
# =========================================================

DEBUG = os.getenv("DEBUG", "True").lower() == "true"


# =========================================================
# Allowed Hosts
# =========================================================

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".chbkn.dev",
    ".chbkn.run",
]


# =========================================================
# CSRF
# =========================================================

CSRF_TRUSTED_ORIGINS = [
    "https://tabadol-nazar.chbkn.dev",
    "https://tabadol-nazar.chbkn.run",
]


# =========================================================
# Applications
# =========================================================

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "axes",

    "accounts",
    "forum",
]


# =========================================================
# Middleware
# =========================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "axes.middleware.AxesMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================================================
# URLs / WSGI
# =========================================================

ROOT_URLCONF = "forum_project.urls"

WSGI_APPLICATION = "forum_project.wsgi.application"


# =========================================================
# Templates
# =========================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates",
        ],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

                "forum.context_processors.forum_categories",
            ],
        },
    },
]


# =========================================================
# Database
# =========================================================

DB_ENGINE = os.getenv("DB_ENGINE", "sqlite").lower()


# ---------------------------------------------------------
# Test Database
# ---------------------------------------------------------

if "test" in sys.argv:

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "test_db.sqlite3",
        }
    }


# ---------------------------------------------------------
# MySQL - Chabokan
# ---------------------------------------------------------

elif DB_ENGINE == "mysql":

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",

            "NAME": os.getenv("DB_NAME"),

            "USER": os.getenv("DB_USER"),

            "PASSWORD": os.getenv("DB_PASSWORD"),

            "HOST": os.getenv("DB_HOST"),

            "PORT": os.getenv("DB_PORT", "3306"),

            "OPTIONS": {
                "charset": "utf8mb4",
            },
        }
    }


# ---------------------------------------------------------
# SQLite - Local Windows
# ---------------------------------------------------------

else:

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",

            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# =========================================================
# Static Files
# =========================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"


STATICFILES_DIRS = []

LOCAL_STATIC_DIR = BASE_DIR / "static"

if LOCAL_STATIC_DIR.exists():
    STATICFILES_DIRS.append(LOCAL_STATIC_DIR)


STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)


# =========================================================
# Media
# =========================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# =========================================================
# Language / Timezone
# =========================================================

LANGUAGE_CODE = "fa-ir"

TIME_ZONE = "Asia/Tehran"

USE_I18N = True

USE_TZ = True


# =========================================================
# Authentication
# =========================================================

LOGIN_URL = "accounts:login"

LOGIN_REDIRECT_URL = "/"

LOGOUT_REDIRECT_URL = "/"


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },

    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),

        "OPTIONS": {
            "min_length": 8,
        },
    },

    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },

    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# =========================================================
# Authentication Backends
# =========================================================

AUTHENTICATION_BACKENDS = [
    "axes.backends.AxesStandaloneBackend",
    "django.contrib.auth.backends.ModelBackend",
]


# =========================================================
# Default Auto Field
# =========================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# =========================================================
# Production Security
# =========================================================

if not DEBUG:

    SECURE_PROXY_SSL_HEADER = (
        "HTTP_X_FORWARDED_PROTO",
        "https",
    )

    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True

    SECURE_CONTENT_TYPE_NOSNIFF = True

    SECURE_REFERRER_POLICY = "same-origin"


# =========================================================
# Django Axes
# =========================================================

AXES_FAILURE_LIMIT = 5

AXES_COOLOFF_TIME = 30

AXES_LOCKOUT_TEMPLATE = "registration/login.html"

AXES_LOCKOUT_PARAMETERS = [
    "username",
    "ip_address",
]

AXES_RESET_ON_SUCCESS = True


# =========================================================
# Email
# =========================================================

EMAIL_BACKEND = (
    "django.core.mail.backends.smtp.EmailBackend"
)

EMAIL_HOST = os.getenv(
    "EMAIL_HOST",
    "smtp.gmail.com",
)

EMAIL_PORT = int(
    os.getenv(
        "EMAIL_PORT",
        "587",
    )
)

EMAIL_USE_TLS = (
    os.getenv(
        "EMAIL_USE_TLS",
        "True",
    ).lower()
    == "true"
)

EMAIL_HOST_USER = os.getenv(
    "EMAIL_HOST_USER",
)

EMAIL_HOST_PASSWORD = os.getenv(
    "EMAIL_HOST_PASSWORD",
)

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SERVER_EMAIL = EMAIL_HOST_USER