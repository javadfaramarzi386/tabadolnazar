#!/usr/bin/env python

#!/usr/bin/env python
"""
مدیریت پروژه جنگو (Django Management Script)
نقطه ورود اجرای دستورات مدیریتی مانند:
- runserver
- makemigrations
- migrate
- createsuperuser
"""

import os
import sys


def main():
    """اجرای دستورات مدیریتی جنگو"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forum_project.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? "
            "Did you forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()