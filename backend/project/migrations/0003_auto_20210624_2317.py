# Generated by Django 3.2.4 on 2021-06-24 23:17
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20210624_2317'),
        ('project', '0002_projectconsumables_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectconsumables',
            options={'verbose_name': 'Материал по проекту: ', 'verbose_name_plural': 'Проектные материалы'},
        ),
        migrations.AlterModelOptions(
            name='projectcurators',
            options={'verbose_name': 'Куратор', 'verbose_name_plural': 'Кураторы'},
        ),
        migrations.AlterField(
            model_name='project',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_contracts', to='customer.contracts', verbose_name='Договор'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='project',
            name='specs',
            field=models.JSONField(verbose_name='Спецификации'),
        ),
        migrations.AlterField(
            model_name='projectconsumables',
            name='consumable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consumables_project', to='project.consumables', verbose_name='Материал'),
        ),
        migrations.AlterField(
            model_name='projectconsumables',
            name='quantity',
            field=models.IntegerField(verbose_name='Количесто'),
        ),
    ]
