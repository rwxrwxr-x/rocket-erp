from django.contrib import admin

from .models import Project
from .models import ProjectDocs


class ProjectDocsInline(admin.TabularInline):
    """Inline class for access to attachments."""

    model = ProjectDocs
    verbose_name = 'Документ'
    verbose_name_plural = 'Документы'
    classes = ['collapse']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin panel settings for Project model."""

    fieldsets = (
        (None, {
            'fields': (
                'title', 'description_brief', 'creator',
                'modified_by'
            ),
        }),
        ('Настройки', {
            'classes': ('collapse',),
            'fields': ('description_full', 'curators', 'created', 'modified'),
        }),
    )
    inlines = [ProjectDocsInline, ]
    readonly_fields = ['creator', 'modified_by', 'created', 'modified']
    search_fields = ('title',)
    list_display = ('title', 'creator', 'created', 'modified', 'modified_by')
