from typing import Union

from crum import get_current_user
from django.db import models
from django.urls import reverse

from ..accounts.models import Account


class TimeStampedModel(models.Model):
    """Abstract base class model that provides created and modified fields."""

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания')
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name='дата последней правки')

    class Meta:
        abstract = True


class Project(TimeStampedModel):
    """Project model."""

    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description_brief = models.CharField(
        max_length=256,
        blank=True,
        default='',
        verbose_name='Краткое описание'
    )

    description_full = models.TextField(
        blank=True,
        default='',
        verbose_name='Описание'
    )

    creator = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None,
        verbose_name='Создатель'
    )

    modified_by = models.ForeignKey(
        Account,
        related_name='Project_modified_by',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None,
        verbose_name='Редактировал'
    )
    file = models.FileField(
        upload_to='projects/uploads',
        blank=True,
        verbose_name='docs'
    )
    curators = models.ManyToManyField(
        Account,
        blank=True,
        related_name='project_curators',
        verbose_name='Кураторы'
    )

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __str__(self): # noqa
        return self.title

    def absolute_url(self) -> Union[str, str]:
        """Get url of current object."""
        return reverse('project', kwargs={'id': self.id})

    def save(self, *args, **kwargs) -> None:
        """Commit current orm object."""
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.creator = user
        self.modified_by = user
        super().save(*args, **kwargs)
