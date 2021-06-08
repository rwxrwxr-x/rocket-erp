from django.urls import path
from django.urls import re_path

from .views import ProjectCreateView
from .views import ProjectListView

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects_list'),
    re_path(r'create/?', ProjectCreateView.as_view(), name='projects_create')
]
