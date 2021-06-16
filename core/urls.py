from django.urls import path
from django.urls import re_path

from .views import about_page
from .views import home_page

urlpatterns = [
    re_path(r'about/?', about_page, name='about'),
    path('', home_page, name='home'),

]
