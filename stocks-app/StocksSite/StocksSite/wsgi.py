"""
WSGI config for StocksSite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
project_folder = os.path.expanduser('~/StocksSite')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StocksSite.settings')

application = get_wsgi_application()
