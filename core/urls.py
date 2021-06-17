from django.urls import path
from django.urls import re_path

from .views import about_page
from .views import home_page
from accounts.views import LogInView, LogOutView
from core.views import handler404

urlpatterns = [
    re_path(r'login/?', LogInView.as_view(), name='login'),
    re_path(r'logout/?', LogOutView.as_view(), name='logout'),
    re_path(r'about/?', about_page, name='about'),
    path('', home_page, name='home'),
    re_path(r'404/?', handler404)

]
