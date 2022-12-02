from django import forms
from .models import Katalog


class KatalogForm(forms.ModelForm):
    class Meta:
        model = Katalog
        fields ='__all__'