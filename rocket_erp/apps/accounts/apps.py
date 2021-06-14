from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Account config."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = "rocket_erp.apps.accounts"
    verbose_name = "profiles"
    verbose_name_plural = "profiles"
