from django.urls import path

from .views import ProjectCreateView
from .views import ProjectItemView
from .views import ProjectListView
from .views import ProjectUpdateView

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects_list'),
    path('create/', ProjectCreateView.as_view(), name='project_create'),
    path('<int:pk>', ProjectItemView.as_view(), name='project_item'),
    path('<int:pk>/edit', ProjectUpdateView.as_view(), name='project_update')
]
