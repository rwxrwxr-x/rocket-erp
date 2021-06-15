from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from ..core.views import TemplateView
from .forms import ProjectCreate
from .forms import ProjectDocsCreate
from .forms import ProjectUpdate
from .models import Project
from .models import ProjectDocs


class ProjectListView(LoginRequiredMixin, ListView):  # noqa
    model = Project
    template_name = 'projects/projects_list.html'
    context_object_name = 'projects'

    def get_queryset(self) -> QuerySet[Project]:
        """Return list of items of this view."""
        query = self.request.GET.get('q')
        if query is not None:
            projects = Project.objects.filter(
                Q(title__icontains=query)
                | Q(description_bfief__icontains=query)
                | Q(category__name__icontains=query)
            ).order_by('-created')
        else:
            projects = Project.objects.order_by('-created')
        return projects


class ProjectItemView(LoginRequiredMixin, DetailView):  # noqa
    template_name = 'projects/projects_item.html'
    model = Project
    context_object_name = 'projects'


class ProjectUpdateView(LoginRequiredMixin,  # noqa
                        TemplateView):
    template_name = 'projects/projects_edit.html'
    model = Project
    minor_models = (ProjectDocs,)
    form_class = ProjectUpdate
    minor_form_classes = (ProjectDocsCreate,)
    success_view_alias = 'project_update'
    success_message = "%(title)s was updated successfully"
    file_attrs = {ProjectDocs: {'action': ProjectDocs.objects.bulk_create,
                                'field': 'file'}}


class ProjectCreateView(LoginRequiredMixin,  # noqa
                        TemplateView):
    template_name = 'projects/projects_edit.html'
    model = Project
    minor_models = (ProjectDocs,)
    form_class = ProjectCreate
    minor_form_classes = (ProjectDocsCreate,)
    success_redirect = reverse_lazy('projects_list')
    success_message = "%(title)s was created successfully"
    file_attrs = {ProjectDocs: {'action': ProjectDocs.objects.bulk_create,
                                'field': 'file'}}
