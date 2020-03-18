"""
WSGI config for flowmeter project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from flowmeter.init import init_role_version, start_flowmeter_server, init_configure

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flowmeter.settings')

init_configure()
init_role_version()
start_flowmeter_server()
application = get_wsgi_application()


