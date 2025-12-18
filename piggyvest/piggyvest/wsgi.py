"""
WSGI config for piggyvest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

# your project path
# project_home = '/home/Alexander2602/pythonrestfulapi'
# if project_home not in sys.path:
#     sys.path.insert(0, project_home)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'piggyvest.settings')

application = get_wsgi_application()
