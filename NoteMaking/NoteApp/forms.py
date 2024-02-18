from django import forms
from .models import Note

class UpdateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']