from django import forms
from .models import Artist, Project

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title', 'status', 'artist', 'number_to_complete', 'number_completed',
            'priority_weight', 'finish_by', 'medium', 'purpose', 'description', 'category'
        ]
