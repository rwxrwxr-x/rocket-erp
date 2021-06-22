"""Integrate with django.contrib.admin module."""
from typing import Any
from typing import Type

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.forms import BaseModelForm
from django.http import HttpRequest

from .models import Account

admin.site.unregister(Group)


@admin.register(Account)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for User model with no email field."""

    def get_form(self, request: HttpRequest, obj: Any = None, **kwargs) -> \
            BaseModelForm:
        """Permissions introduction, TO DO."""
        if request.user.is_superuser:
            self.fieldsets += ((None, {"fields": ("email", "password")}),)
            return super().get_form(request, obj, **kwargs)
        elif request.user.is_staff:
            self.fieldsets += ((None, {"fields": ("email", "password")}),)
            return super().get_form(request, obj, **kwargs)

    fieldsets: tuple = (
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "second_name",
                    "last_name",
                    "birthday",
                    "avatar",
                    "about",
                    "phone",
                    "is_deleted",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets: tuple = (
        (
            None,
            {
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    list_display: tuple = (
        "email",
        "pk",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "is_deleted",
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)


@admin.register(Group)
class GroupsAdmin(admin.ModelAdmin):
    """Overriding a Groups admin model."""

    list_display = ["name", "pk"]

    class Meta:
        model: Type[Group] = Group


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    """Overriding a Permission admin model."""

    list_display = ["name", "content_type"]

    class Meta:
        model: Type[Permission] = Permission


@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    """Overriding a ContentType admin model."""

    class Meta:
        model: Type[ContentType] = ContentType