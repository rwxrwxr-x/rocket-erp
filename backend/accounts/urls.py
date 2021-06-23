from django.urls import re_path, path
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import LogoutView, TestView, ProfileView

urlpatterns = [
    re_path(r"^jwt/?$", TokenObtainPairView.as_view(), name="login"),
    re_path(r"^jwt/refresh/?$", TokenRefreshView.as_view(), name="logout"),
    re_path(r"^jwt/logout/?$", LogoutView.as_view()),
    re_path(r"^jwt/test/?$", TestView.as_view()),
    re_path(r"^jwt/verify/?$", TokenVerifyView.as_view()),
    re_path(r"^profile/?$", ProfileView.as_view()),
    path("admin", admin.site.urls),
]
