from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email: str = '',
                     password: str = '', **extra_fields):
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email: str, password: str = None, **extra_fields) \
            -> AbstractUser:
        """Create and save a regular User with given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields) \
            -> AbstractUser:
        """Create and save a superuser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class Account(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    avatar = models.ImageField(
        upload_to="avatars/", blank=True, null=True, verbose_name="avatar"
    )

    second_name = models.CharField(
        blank=True, verbose_name="surname", null=True, max_length=50
    )

    about = models.TextField(blank=True, verbose_name="description", null=True,
                             max_length=350)

    birthday = models.DateTimeField(null=True, blank=True,
                                    verbose_name="birthday")

    phone = models.CharField(max_length=11, null=True, blank=True,
                             verbose_name="phone")

    is_deleted = models.BooleanField(default=False, verbose_name="deleted")

    updated = models.DateTimeField(auto_now=True, verbose_name="updated")

    objects = UserManager()

    def __str__(self) -> str:
        """Return str(self)."""
        return " ".join([self.first_name, self.last_name])