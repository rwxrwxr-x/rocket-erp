from django.urls import path

from .views import MyProfile
from .views import MyProfileUpdate

app_name = "accounts"

urlpatterns = [
    path('<int:pk>', MyProfile.as_view(), name="myprofile"),
    path('profileupdate/<int:pk>', MyProfileUpdate.as_view(),
         name="profileupdate"),
]
