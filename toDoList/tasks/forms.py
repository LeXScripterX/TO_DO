from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    """Formulario para crear y actualizar objetos Task."""

    class Meta:
        model = Task
        fields = ['title', 'description', 'status']

    def clean_title(self):
        """Valida que el título no esté vacío."""
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('El título no puede estar vacío.')
        return title