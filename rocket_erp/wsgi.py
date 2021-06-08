import os

from django.core.wsgi import get_wsgi_application
from django.core.wsgi import WSGIHandler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rocket_erp.settings")

app: WSGIHandler = get_wsgi_application()
