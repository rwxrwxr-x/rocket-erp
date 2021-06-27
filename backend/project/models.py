from django.db import models

from ..accounts.models import Account
from ..customer.models import Contracts


# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name='Наименование',
                            max_length=100)
    specs = models.JSONField(verbose_name='Спецификации')
    contract = models.ForeignKey(Contracts,
                                 verbose_name='Договор',
                                 on_delete=models.CASCADE,
                                 related_name='projects',
                                 related_query_name='project')
    is_cancelled = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class ProjectCurators(models.Model):
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name='project_curator')
    account = models.ForeignKey(Account,
                                on_delete=models.CASCADE,
                                related_name='curated_projects')

    def __str__(self):
        return f'Куратор проекта {self.id}, ' \
               f'по договору {self.project.contract.name}'

    class Meta:
        verbose_name = 'Куратор'
        verbose_name_plural = 'Кураторы'


class Consumables(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    specs = models.JSONField()
    note = models.CharField(max_length=100)
    avg_delivery_time = models.TimeField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class ProjectConsumables(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='project_consumables')
    consumable = models.ForeignKey(Consumables,
                                   verbose_name='Материал',
                                   on_delete=models.CASCADE,
                                   related_name='consumables_project')
    quantity = models.IntegerField(verbose_name='Количесто')

    def __str__(self):
        return f'{self.project.name}'

    class Meta:
        verbose_name = 'Материал по проекту: '
        verbose_name_plural = 'Проектные материалы'
