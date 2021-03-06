# Generated by Django 3.2.4 on 2021-06-24 23:17
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_customer_jp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankdetail',
            name='account',
            field=models.CharField(default='', max_length=30, verbose_name='р/с'),
        ),
        migrations.AlterField(
            model_name='bankdetail',
            name='bic',
            field=models.CharField(default='', max_length=32, verbose_name='БИК'),
        ),
        migrations.AlterField(
            model_name='bankdetail',
            name='c_account',
            field=models.CharField(default='', max_length=28, verbose_name='к/c'),
        ),
        migrations.AlterField(
            model_name='bankdetail',
            name='name',
            field=models.CharField(default='', max_length=35, verbose_name='Банк'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(blank=True, default='', max_length=15, verbose_name='Фактический адрес'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='inn',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='jp',
            field=models.CharField(choices=[('FP', 'Физлицо'), ('JP', 'ООО')], max_length=3, verbose_name='Тип юрлица'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='kpp',
            field=models.CharField(blank=True, default='', max_length=25, verbose_name='КПП'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default='', max_length=35, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='okpo',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='ОКПО'),
        ),
    ]
