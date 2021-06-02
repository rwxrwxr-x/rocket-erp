from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import DetailView, FormView, UpdateView, View

from .forms import ProfileForm, SingInViaEmailForm
from .models import Account
from .utils import same_user


class GuestOnlyView(View):
    """Guest only access for view."""

    def dispatch(self, request, *args, **kwargs):
        """Override of View dispatch method."""
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)

        return super().dispatch(request, *args, **kwargs)


class LogInView(GuestOnlyView, FormView):
    """Generic login for users."""

    template_name = "accounts/login.html"

    @staticmethod
    def get_form_class(**kwargs):
        """Sing in with email form."""
        if settings.LOGIN_VIA_EMAIL:
            return SingInViaEmailForm

    @method_decorator(sensitive_post_parameters("password"))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        """Override of View dispatch method."""
        request.session.set_test_cookie()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """Override of View form_valid method."""
        request = self.request

        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()

        if settings.USE_REMEMBER_ME:
            if not form.cleaned_data["remember_me"]:
                request.session.set_expiry(0)

        login(request, form.user_cache)

        redirect_to = request.POST.get(
            REDIRECT_FIELD_NAME, request.GET.get(REDIRECT_FIELD_NAME)
        )
        url_is_safe = is_safe_url(
            redirect_to,
            allowed_hosts=request.get_host(),
            require_https=request.is_secure(),
        )
        if url_is_safe:
            return redirect(redirect_to)

        return redirect(settings.LOGIN_REDIRECT_URL)


class LogOutView(BaseLogoutView):
    """Generic logout for users."""

    next_page = "home"

    def get(self, request, *args, **kwargs):
        """Override of basic get method."""
        logout(request)
        return super().get(request, *args, **kwargs)


class MyProfile(LoginRequiredMixin, DetailView):
    """User profile view."""

    model = Account
    context_object_name = "user"
    template_name = "accounts/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("accounts:myprofile")

    def get_success_url(self):
        """Redirect with current user id."""
        return reverse_lazy("accounts:myprofile",
                            kwargs={"pk": self.object.pk})


@method_decorator(same_user, "get")
class MyProfileUpdate(LoginRequiredMixin, UpdateView):
    """User update profile view."""

    model = Account
    template_name = "accounts/profileupdate.html"
    form_class = ProfileForm
    success_url = reverse_lazy("accounts:profileupdate")

    def get_success_url(self):
        """Redirect with current user id."""
        return reverse_lazy("accounts:profileupdate",
                            kwargs={"pk": self.object.pk})
