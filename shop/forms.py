from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'corporate', 'image', 'position', 'my_skills','needed_skills','bio','gender','age','email']