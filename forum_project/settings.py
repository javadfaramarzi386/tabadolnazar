# forum_project/setting.py

# SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-dzh0^t5i#)cvq^u-gb^1to@8bp+ygt8l(b1w^stti%(o&wded1')
# "PASSWORD": "DonoB8iwu5iB",

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

# =============================================================================
# مسیرهای پایه پروژه
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# =============================================================================
# تنظیمات امنیتی
# =============================================================================

# کلید مخفی پروژه (به هیچ وجه در گیت آپلود نشود)
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-dzh0^t5i#)cvq^u-gb^1to@8bp+ygt8l(b1w^stti%(o&wded1')   # در تولید حتماً از محیط استفاده کنید

# حالت دیباگ (در محیط تولید حتماً False باشد)
DEBUG = False

# هاست‌هایی که اجازه دسترسی دارند
ALLOWED_HOSTS = [
    '.chbkn.run',
    'tabadolnazar.chbkn.run',
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

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "tabadolnazar737_daniel",
        "USER": "tabadolnazar737_daniel",
        "PASSWORD": "DonoB8iwu5iB",
        "HOST": "services.irn10.chabokan.net",
        "PORT": "31237",
        "OPTIONS": {
            "charset": "utf8mb4",
        },
    }
}

# =============================================================================
# فایل‌های استاتیک و رسانه
# =============================================================================

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

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
    # SECURE_SSL_REDIRECT = True   # در صورت نیاز فعال کنید