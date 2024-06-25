from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProfileModel
from django import forms

class InscriptionForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(InscriptionForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None   # Supprime les lignes de textes pour aider !

class UtilisateurUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(UtilisateurUpdate, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email']:
            self.fields[fieldname].help_text = None   # Supprime les lignes de textes pour aider !

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['image']
