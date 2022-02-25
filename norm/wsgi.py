"""
WSGI config for norm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, "/var/www/venv_norm/lib/python3.8/site-packages")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'norm.settings')

application = get_wsgi_application()
