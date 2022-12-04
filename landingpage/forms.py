from django import forms
from .models import Konten


class KontenForm(forms.ModelForm):
    class Meta:
        model = Konten
        fields ='__all__'