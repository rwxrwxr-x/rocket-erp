from typing import Any

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def home_page(request: HttpRequest) -> HttpResponse:
    """Home page view."""
    template = loader.get_template("home.html")
    context: dict[Any, Any] = {}
    return HttpResponse(template.render(context, request))


def about_page(request: HttpRequest) -> HttpResponse:
    """About page view."""
    template = loader.get_template("about.html")
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
