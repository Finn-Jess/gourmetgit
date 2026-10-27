from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'category', 'prep_time', 'ingredients', 'instructions']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter recipe title...'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'prep_time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Time in minutes'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'List ingredients separated by commas...'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Step-by-step instructions...'}),
        }
        help_texts = {
            'prep_time': 'Enter total preparation time in whole minutes.',
        }

    def clean_prep_time(self):
        prep_time = self.cleaned_data.get('prep_time')
        if prep_time is not None and prep_time <= 0:
            raise forms.ValidationError("Preparation time must be greater than zero minutes.")
        return prep_time

class RecipeReadOnlyForm(RecipeForm):
    """Form demonstrating read-only or disabled fields requirement."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].disabled = True