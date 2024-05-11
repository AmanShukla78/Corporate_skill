from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'corporate', 'image', 'position', 'my_skills','needed_skills','bio','gender','age','email']

# workdemo
class WorkdemoForm(forms.ModelForm):
    class Meta:
        model = Workdemo
        fields = '__all__'
        exclude = ['user']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ['created_at']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = ['userB']
    
class ShareSkillForm(forms.ModelForm):
    class Meta:
        model = ShareSkill
        fields = '__all__'
        exclude = ['userA']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        exclude = ['userA']
