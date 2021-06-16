from django import forms
from django.conf import settings
from django.forms import CharField
from django.forms import EmailField
from django.forms import EmailInput
from django.forms import FileInput
from django.forms import NumberInput
from django.forms import PasswordInput
from django.forms import Textarea
from django.forms import TextInput
from django.forms import ValidationError

from .models import Account


class UserCacheMixin: # noqa
    user_cache = None


class SingIn(UserCacheMixin, forms.Form):
    """Basic auth form."""

    password = CharField(label="Password", strip=False, widget=PasswordInput)

    def __init__(self, *args, **kwargs) -> None:
        """Auth model constructor."""
        super().__init__(*args, **kwargs)

        if settings.USE_REMEMBER_ME:
            self.fields["remember_me"] = forms.BooleanField(
                label="Remember me", required=False
            )

    def clean_password(self) -> str:
        """Check password for correctness."""
        password = self.cleaned_data["password"]

        if not self.user_cache:
            return password

        if not self.user_cache.check_password(password):
            raise ValidationError("Wrong password")

        return password


class SingInViaEmailForm(SingIn):
    """Auth form with email."""

    email = EmailField(label="Email")

    @property
    def field_order(self) -> list:
        """Auth fields, by settings.USE_REMEMBER_ME."""
        if settings.USE_REMEMBER_ME:
            return ["email", "password", "remember_me"]
        return ["email", "password"]

    def clean_email(self) -> str:
        """Clean check of email."""
        email = self.cleaned_data["email"]

        user: Account = Account.objects.filter(email__iexact=email).first()

        if not user:
            raise ValidationError("Wrong email")

        if not user.is_active:
            raise ValidationError("This acc not activated")

        self.user_cache: None = user

        return email


class ProfileForm(forms.ModelForm):
    """UserProfile form based on Account model."""

    class Meta:
        model = Account
        fields = ["first_name", "last_name", "email", "phone", "avatar",
                  "about"]

        widgets = {
            "first_name": TextInput(attrs={"class": "input"}),
            "second_name": TextInput(attrs={"class": "input"}),
            "last_name": TextInput(attrs={"class": "input"}),
            "email": EmailInput(attrs={"class": "input"}),
            "phone": NumberInput(attrs={"class": "input"}),
            "avatar": FileInput(attrs={"class": "input"}),
            "about": Textarea(attrs={"class": "input"}),
        }
