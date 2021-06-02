from django.urls import path

from .views import LogInView, LogOutView, MyProfile, MyProfileUpdate

app_name = "accounts"

urlpatterns = [
    path("login/", LogInView.as_view(), name="login"),
    path("logout/", LogOutView.as_view(), name="logout"),
    path("<int:pk>", MyProfile.as_view(), name="myprofile"),
    path("profileupdate/<int:pk>", MyProfileUpdate.as_view(),
         name="profileupdate"),
]
