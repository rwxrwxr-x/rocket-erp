from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include
from django.urls import path

from .views import about_page
from .views import home_page

handler404 = "rocket_erp.views.handler404"
handler403 = "rocket_erp.views.handler403"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("rocket_erp.apps.api.urls")),
    path("accounts/", include("rocket_erp.apps.accounts.urls")),
    path("about", about_page, name="about"),
    path("", home_page, name="home"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
