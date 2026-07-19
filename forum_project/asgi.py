# forum_project/asgi.py

import os

from django.core.asgi import get_asgi_application


# این متغیر باید قبل از ساخت application تنظیم شود تا Django تنظیمات پروژه را بشناسد.
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "forum_project.settings",
)

application = get_asgi_application()