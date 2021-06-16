from functools import wraps
from typing import Callable

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_mail(to, template, context):
    """
    Email sending function.

    :param to: destination
    :param template: html or txt
    :param context: msg
    """
    html_content = render_to_string(f"accounts/emails/{template}.html",
                                    context)
    text_content = render_to_string(f"accounts/emails/{template}.txt",
                                    context)

    msg = EmailMultiAlternatives(
        context["subject"], text_content, settings.DEFAULT_FROM_EMAIL, [to]
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def same_user(view_func: Callable):
    """Decorate for restrict user access to profiles."""
    @wraps(view_func)
    def _wrapped_view(request, pk, *args, **kwargs):
        if request.user.id != pk:
            raise PermissionDenied
        else:
            return view_func(request, pk, *args, **kwargs)

    return _wrapped_view
