from django import forms
from .models import Promo

class PromoForm(forms.ModelForm) :
    class Meta :
        model = Promo
        fields = '__all__'


    tanggalExp = forms.DateField(label = "Tanggal Berakhir", required= True,
    widget= forms.DateInput(attrs={'type' : 'date'}))