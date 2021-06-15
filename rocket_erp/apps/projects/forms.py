from django.forms import ModelForm
from django.forms import Textarea
from django.forms import TextInput

from ..core.widgets import ClearableFileInput
from .models import Project
from .models import ProjectDocs


class ProjectCreate(ModelForm):  # noqa
    class Meta:
        model = Project
        fields = ['title', 'description_brief', 'description_full']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description_brief': Textarea(attrs={'class': 'form-control'}),
            'description_full': Textarea(attrs={'class': 'form-control'}),
        }


class ProjectDocsCreate(ModelForm): # noqa
    class Meta:
        model = ProjectDocs
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(
                attrs={'class': 'form-control', 'multiple': True}
            )
        }

class ProjectUpdate(ProjectCreate): # noqa
    def __init__(self, *args, **kwargs): # noqa
        super().__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['title'].widget.attrs['readonly'] = True
