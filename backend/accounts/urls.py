from django.contrib import admin
from django.urls import path
from django.urls import re_path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

from .views import LogoutView
from .views import ProfileView
from .views import TestView

urlpatterns = [
    re_path(r"^jwt/?$", TokenObtainPairView.as_view(), name="login"),
    re_path(r"^jwt/refresh/?$", TokenRefreshView.as_view(), name="logout"),
    re_path(r"^jwt/logout/?$", LogoutView.as_view()),
    re_path(r"^jwt/test/?$", TestView.as_view()),
    re_path(r"^jwt/verify/?$", TokenVerifyView.as_view()),
    re_path(r"^profile/?$", ProfileView.as_view()),
    path("admin", admin.site.urls),
]
