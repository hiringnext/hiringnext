from django import forms
from .models import LookingForJob


class LookingForJobForm(forms.ModelForm):
    class Meta:
        model = LookingForJob
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }
        fields = '__all__'
