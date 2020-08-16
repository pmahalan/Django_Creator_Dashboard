from django import forms
from .models import Creator

class CreatorForm(forms.ModelForm):

    class Meta:
        model = Creator
        fields = ["name","upload"]