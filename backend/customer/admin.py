from django.contrib import admin

from .models import BankDetail
from .models import Contracts
from .models import Customer


# Register your models here.
class BankDetails(admin.TabularInline):
    model = BankDetail
    verbose_name = 'Реквизиты'
    classes = ['collapse']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Admin panel settings for Project model."""

    fieldsets = (
        (None, {
            'fields': (
                'email', 'name', 'jp', 'address', 'inn',
            ),
        }),
        (None, {
            'classes': ('additional',),
            'fields': ('kpp', 'okpo'),
        }),
    )
    inlines = (BankDetails,)
    search_fields = ('name', 'inn')
    list_display = ('name', 'id')


@admin.register(Contracts)
class ContractsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'customer')
        }),)
    search_fields = ('name', 'customer')
    list_display = ('name', 'customer')
