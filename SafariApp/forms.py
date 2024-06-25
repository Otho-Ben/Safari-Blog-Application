# la forme du poste
from django import forms
from .models import Safari_Post

class PosteModelForm(forms.ModelForm):
    main = forms.CharField(widget=forms.Textarea(attrs={'rows': 5})) # Rèduire la case du main pour une meilleur vue.
    class Meta:
        model = Safari_Post
        fields = ('titre', 'main')