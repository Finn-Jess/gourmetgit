from django import forms
from .models import Workshop

class WorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = ['title', 'instructor', 'date', 'recipes']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Workshop title...'}),
            'instructor': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'recipes': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
        }
        help_texts = {
            'recipes': 'Hold Control (Cmd on Mac) to select multiple recipes.',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Workshop title must be at least 5 characters long.")
        return title