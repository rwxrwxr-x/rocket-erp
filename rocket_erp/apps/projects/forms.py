from django import forms
from django.forms import FileInput
from django.forms import Textarea
from django.forms import TextInput

from .models import Project


class ProjectCreate(forms.ModelForm): # noqa
    class Meta:
        model = Project
        fields = ['title', 'description_brief', 'description_full', 'file']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description_brief': Textarea(attrs={'class': 'form-control'}),
            'description_full': Textarea(attrs={'class': 'form-control'}),
            'file': FileInput(attrs={'class': 'form-control'})
        }
