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

from ..core.utils import get_fk_by_instance
from ..core.utils import get_model


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


def handler500(request: HttpRequest, *args, **kwargs) -> HttpResponse:  # noqa
    return error(request, 500, 'Server error', *args, **kwargs)


class TemplateView(FormView, SingleObjectTemplateResponseMixin,
                   ModelFormMixin):
    """
    TemplateView for making views with create/update actions with minor model.

    Action depends on pk variable of model.
    - **attributes**::
        :str template_name: path to template file
        :ModelForm form_class: main form
        :Model model: main model
        :tuple minor_models: minor models, with fk to main model
        :minor_form_classes: forms
        :prefix: str: forms prefix
        :object: Type[model]: current object of main model
        :success_redirect:
        :success_message:
        :view_alias:
        :file_attrs: attributes for file-input
    """

    template_name: str = ''
    form_class: Type[ModelForm] = None
    model: Type[Model] = None
    minor_models: tuple[Model] = None
    minor_form_classes: tuple[ModelForm] = None
    prefix: str = 'form_'
    object: Type[model] = None
    success_redirect: str = '#'
    success_message: str = ''
    success_view_alias: str = ''
    file_attrs: dict[dict[str, Any]] = None

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
        forms: list[Form] = [self.get_form()]
        forms[1:] = list(map(
            lambda _form, _model:
            _form(**{'instance': _model(self.object)},
                  **{'data': self.request.POST}
                  if _model not in self.file_attrs.keys()
                  else {'files': self.request.FILES}),
            self.minor_form_classes,
            self.minor_models
        ))
        if False not in list(map(lambda x: x.is_valid(), forms)):
            return self.form_valid(forms)
        else:
            messages.error(request, 'Form error', extra_tags='Err')
            return self.form_invalid(forms)

    def form_invalid(self, forms: list[Form]) -> TemplateResponse:
        """If the forms invalid, render invalid form."""
        context = {'files': forms[0]}
        context.update(zip(list(map(lambda x: x.__name__.lower(),
                                    self.minor_models)),
                           forms[1:]))
        return self.render_to_response(self.get_context_data(**context))

    def form_valid(self, forms: list[Form]) -> HttpResponseRedirect:
        """If form is valid, saving the associated models."""
        self.object = forms[0].save()

        for form in forms[1:]:
            instance: object = form.instance
            if get_model(instance) in self.file_attrs.keys():
                self.file_attrs[get_model(instance)]['action']([
                    get_model(instance)(
                        **{get_fk_by_instance(instance): self.object.pk,
                           self.file_attrs[get_model(instance)][
                               'field']: file})
                    for file in self.request.FILES.getlist('file')
                ])
                continue
            setattr(instance, get_fk_by_instance(instance), self.object.pk)
            form.save()

        self.send_success_message(forms[0])
        return HttpResponseRedirect(self.get_success_url())

    def send_success_message(self, form: Form) -> None:
        """Add success message to contrib.messages."""
        success_message: str = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)

    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        """Get the success message."""
        return self.success_message % cleaned_data

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        """Insert forms(form_class, minor_forms) into context dict."""
        context: dict = dict()
        context['form'] = self.get_form()
        for model, form in zip(self.minor_models, self.minor_form_classes):
            context[model.__name__.lower()] = form
        if self.object:
            context['object'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super(FormMixin, self).get_context_data(**context)

    def get_success_url(self) -> Union[HttpResponseRedirect, str]:
        """Return the URL to redirect to after processing a valid form."""
        if self.success_view_alias and self.object:
            return reverse_lazy(self.success_view_alias,
                                kwargs={'pk': self.object.pk})
        else:
            return self.success_redirect
