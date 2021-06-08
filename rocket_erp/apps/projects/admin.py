from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin panel settings for Project model."""

    fieldsets = (
        (None, {
            'fields': (
                'title', 'description_brief', 'creator', 'curators',
                'modified_by', 'created', 'modified'
            ),
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('description_full',),
        }),
    )
    readonly_fields = ['creator', 'modified_by', 'created', 'modified']
    search_fields = ('title',)
    list_display = ('title', 'creator', 'created', 'modified', 'modified_by')
