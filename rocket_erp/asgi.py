import os

from django.core.asgi import ASGIHandler
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rocket_erp.settings")

app: ASGIHandler = get_asgi_application()
