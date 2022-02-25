from django import forms
from .models import NormForm


class NormFormForm(forms.ModelForm):
    class Meta:
        model = NormForm
        fields = '__all__'
