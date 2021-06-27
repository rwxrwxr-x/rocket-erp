from django.contrib import admin

from .models import Consumables
from .models import Project
from .models import ProjectConsumables
from .models import ProjectCurators


class ProjectCuratorsAdmin(admin.TabularInline): # noqa
    model = ProjectCurators
    classes = ('collapse',)
    raw_id_fields = ('account',)


class ProjectConsumablesAdmin(admin.StackedInline): # noqa
    model = ProjectConsumables
    raw_id_fields = ('consumable',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin): # noqa
    fieldsets = (
        (None, {
            'fields': (
                'name', 'specs', 'contract', 'is_cancelled', 'is_completed'
            )
        }),
    )
    raw_id_fields = ('contract',)
    inlines = (ProjectCuratorsAdmin, ProjectConsumablesAdmin)
    search_fields = ('name', 'contract', 'project_consumables')
    list_display = ('name', 'contract')


@admin.register(Consumables)
class ConsumablesAdmin(admin.ModelAdmin): # noqa
    fieldsets = (
        (None, {
            'fields': (
                'name', 'manufacturer', 'url', 'price', 'specs', 'note',
                'avg_delivery_time')
        }),
    )
    search_fields = ('name', 'manufacturer')
