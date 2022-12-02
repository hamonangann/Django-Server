from django import forms
from .models import Promo

class PromoForm(forms.ModelForm) :
    class Meta :
        model = Promo
        fields = '__all__'