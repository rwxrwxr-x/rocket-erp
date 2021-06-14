from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include
from django.urls import path
from django.urls import re_path

handler404 = 'rocket_erp.apps.core.views.handler404'
handler403 = 'rocket_erp.apps.core.views.handler403'
handler500 = 'rocket_erp.apps.core.views.handler500'

urlpatterns = [
    re_path(r'admin/?', admin.site.urls),
    path('api/', include('rocket_erp.apps.api.urls')),
    path(r'accounts/', include('rocket_erp.apps.accounts.urls')),
    path('', include('rocket_erp.apps.core.urls')),
    path('projects/', include('rocket_erp.apps.projects.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
