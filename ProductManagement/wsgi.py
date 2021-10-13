"""
WSGI config for ProductManagement project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProductManagement.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.development')

application = get_wsgi_application()
