from django import forms
from .models import Profile

class Resume(forms.ModelForm):
    class Meta:
        model=Profile
        fields= '__all__'
