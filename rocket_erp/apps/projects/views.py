from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.db.models import QuerySet
from django.forms import forms
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .forms import ProjectCreate
from .models import Project


class ProjectListView(LoginRequiredMixin, ListView): # noqa
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


class ProjectCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView): # noqa
    model = Project
    template_name = 'projects/projects_create.html'
    form_class = ProjectCreate
    context_object_name = 'projects'
    success_url = reverse_lazy('projects_list')
    success_message = '%(title) создан'

    def form_valid(self, form: forms) -> HttpResponse:
        """If the form is valid, save object of model."""
        return super().form_valid(form)
