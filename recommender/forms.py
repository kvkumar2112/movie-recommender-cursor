from django import forms
from .models import UserPreference, Rating

class UserPreferenceForm(forms.ModelForm):
    class Meta:
        model = UserPreference
        fields = ['preferred_genres', 'min_rating', 'min_release_year']
        widgets = {
            'preferred_genres': forms.TextInput(attrs={'placeholder': 'e.g., Action, Drama, Comedy'}),
            'min_rating': forms.NumberInput(attrs={'min': 0, 'max': 10, 'step': 0.1}),
            'min_release_year': forms.NumberInput(attrs={'min': 1900, 'max': 2025}),
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 10, 'step': 0.5}),
        } 