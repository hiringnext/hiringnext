from django import forms
from .models import ReferClient


class ClientReferForm(forms.ModelForm):
    class Meta:
        model = ReferClient
        fields = '__all__'
        exclude = ('created_date',)
