# forum_project/setting.py


# =============================================================================
# forum_project/settings.py
# =============================================================================
"""
تنظیمات اصلی پروژه forum_project (سایت تبادل نظر)

این فایل قلب تپنده پروژه است و تمام تنظیمات پایه، امنیتی، دیتابیس،
فایل‌های استاتیک و رسانه و غیره را مدیریت می‌کند.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# =============================================================================
# مسیرهای پایه پروژه
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# =============================================================================
# تنظیمات امنیتی
# =============================================================================

# کلید مخفی پروژه (به هیچ وجه در گیت آپلود نشود)
SECRET_KEY = os.getenv("SECRET_KEY")

# حالت دیباگ (در محیط تولید حتماً False باشد)
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# هاست‌هایی که اجازه دسترسی دارند
ALLOWED_HOSTS = [
    '.chbkn.run',
    'tabadolnazar.chbkn.run',
    '.chbkn.dev',
    'tabadolnazar.chbkn.dev',
    '127.0.0.1',
    'localhost',
]

# برای امنیت CSRF در دامنه‌های خارجی
CSRF_TRUSTED_ORIGINS = [
    "https://tabadolnazar.chbkn.run",
]

# =============================================================================
# اپلیکیشن‌های نصب شده
# =============================================================================

INSTALLED_APPS = [
    # اپ‌های شخص ثالث (باید قبل از اپ‌های جنگو باشند)
    'whitenoise.runserver_nostatic',

    # اپ‌های پیش‌فرض جنگو
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'axes',
    # اپ‌های پروژه شما
    'accounts',
    'forum',

    # اپ‌های اختیاری
    # 'django_extensions',        # برای ابزارهای توسعه (shell_plus و غیره)
]

# =============================================================================
# Middlewareها (میان‌افزارها)
# =============================================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # برای سرو استاتیک در تولید
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'axes.middleware.AxesMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'forum_project.urls'
WSGI_APPLICATION = 'forum_project.wsgi.application'

# =============================================================================
# قالب‌ها (Templates)
# =============================================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],   # قالب‌های اصلی پروژه
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

# =============================================================================
# دیتابیس
# =============================================================================

DB_ENGINE = os.getenv("DB_ENGINE", "sqlite")

if DB_ENGINE == "mysql":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.getenv("DB_NAME"),
            "USER": os.getenv("DB_USER"),
            "PASSWORD": os.getenv("DB_PASSWORD"),
            "HOST": os.getenv("DB_HOST"),
            "PORT": os.getenv("DB_PORT"),
            "OPTIONS": {
                "charset": "utf8mb4",
            },
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# =============================================================================
# فایل‌های استاتیک و رسانه
# =============================================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = []

if (BASE_DIR / "static").exists():
    STATICFILES_DIRS.append(BASE_DIR / "static")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"
# =============================================================================
# تنظیمات بین‌المللی و زمانی
# =============================================================================

LANGUAGE_CODE = 'fa-ir'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True

# =============================================================================
# احراز هویت
# =============================================================================

LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
# =============================================================================
# اعتبارسنجی رمز عبور
# =============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 8,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
# =============================================================================
# Authentication Backends
# =============================================================================

AUTHENTICATION_BACKENDS = [
    "axes.backends.AxesStandaloneBackend",
    "django.contrib.auth.backends.ModelBackend",
]

# =============================================================================
# فیلد پیش‌فرض
# =============================================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =============================================================================
# تنظیمات امنیتی برای تولید (Production)
# =============================================================================

if not DEBUG:

    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True

    SECURE_BROWSER_XSS_FILTER = True

    SECURE_CONTENT_TYPE_NOSNIFF = True

    SECURE_REFERRER_POLICY = "same-origin"
    # SECURE_SSL_REDIRECT = True
    # در صورت نیاز فعال کنید
# =============================================================================
# تنظیمات امنیت ورود (django-axes)
# =============================================================================

# حداکثر تعداد تلاش ناموفق برای ورود
AXES_FAILURE_LIMIT = 5

# مدت زمان قفل شدن (۳۰ دقیقه)
AXES_COOLOFF_TIME = 30

# بعد از قفل شدن، کاربر به صفحه ورود برگردد
AXES_LOCKOUT_TEMPLATE = 'registration/login.html'

# شناسایی بر اساس IP و نام کاربری
AXES_LOCKOUT_PARAMETERS = ["username", "ip_address"]

# بعد از ورود موفق، شمارنده خطا صفر شود
AXES_RESET_ON_SUCCESS = True