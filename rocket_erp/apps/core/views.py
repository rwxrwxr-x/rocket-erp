from typing import Any
from typing import Type
from typing import Union

from django.contrib import messages
from django.db.models import Model
from django.forms import Form
from django.forms import ModelForm
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import FormMixin
from django.views.generic.edit import ModelFormMixin


def home_page(request: HttpRequest) -> HttpResponse:
    """Home page view."""
    template = loader.get_template("core/home.html")
    context: dict[Any, Any] = {}
    return HttpResponse(template.render(context, request))


def about_page(request: HttpRequest) -> HttpResponse:
    """About page view."""
    template = loader.get_template("core/about.html")
    context = {"text": "hello"}
    return HttpResponse(template.render(context, request))


def error(request: HttpRequest, code: int, text: str, *args, **kwargs) \
        -> HttpResponse:
    """Template error view, for handlers."""
    return render(
        request,
        "error.html",
        context={"error": {"code": code, "text": text}},
        content_type="text/html",
    )


def handler404(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    """Not found error handler."""
    return error(request, 404, "Page not found", *args, **kwargs)


def handler403(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    """Permission error handler."""
    return error(request, 403, "Not accessed", *args, **kwargs)


def handler500(request: HttpRequest, *args, **kwargs) -> HttpResponse: # noqa
    return error(request, 500, 'Server error', *args, **kwargs)


class TemplateView(FormView, SingleObjectTemplateResponseMixin,
                   ModelFormMixin):
    """
    TemplateView for making views with create/update actions with minor model.

    Action depends on pk variable of model.
    """

    template_name: str = ''
    form_class: Type[ModelForm] = None
    model: Type[Model] = None
    minor_models = None
    minor_form_classes = None
    prefix: str = 'form_'
    object: Type[model] = None
    success_redirect: str = '#'
    view_alias: str = ''
    _data = None

    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.

        Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """
        try:
            obj = super().get_object(queryset)
        except AttributeError:
            obj = None
        return obj

    def get(self, request, *args, **kwargs) -> TemplateResponse:
        """Handle GET requests: instantiate a blank version of the form."""
        self.object = self.get_object()
        context: dict[str, Any] = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
        """
        Handle POST requests.

        Instantiate a form and file_form instances with the passed POST
        variables and then check if it's valid.
        """
        self.object = self.get_object()
        form: Form = self.get_form()
        file_form: Form = self.minor_form_classes(
            instance=self.minor_models(),
            files=self.request.FILES)
        form.errors.update(file_form.errors)
        if form.is_valid() and file_form.is_valid():
            return self.form_valid(form)
        else:
            messages.error(request,
                           next(iter(file_form.errors.values())),
                           extra_tags='Error message')
            return self.form_invalid(form)

    def form_valid(self, form) -> HttpResponseRedirect:
        """If form is valid, saving the associated models."""
        self.object = form.save()
        files = self.request.FILES.getlist('file')
        self.minor_models.objects.bulk_create([
            self.minor_models(file=file, project=self.object) for
            file in files
        ])
        return super(ModelFormMixin, self).form_valid(form)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        """Insert forms(form_class, file_form_class) into context dict."""
        context: dict = dict()
        context['form'] = self.get_form()
        context['attach'] = self.minor_form_classes
        if self.object:
            context['object'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super(FormMixin, self).get_context_data(**context)

    def get_success_url(self) -> Union[HttpResponseRedirect, str]:
        """Return the URL to redirect to after processing a valid form."""
        if self.view_alias and self.object:
            return reverse_lazy(self.view_alias,
                                kwargs={'pk': self.object.pk})
        else:
            return self.success_redirect
