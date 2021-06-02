from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

from .views.accounts import AccountViewSet

router = DefaultRouter()
router.register("user", AccountViewSet)

jwt_urlpatterns = [
    path("auth-jwt/", obtain_jwt_token),
    path("auth-jwt-refresh/", refresh_jwt_token),
    path("auth-jwt-verify/", verify_jwt_token),
]

urlpatterns = router.urls
