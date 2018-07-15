from django import forms
from .models import Car

class Creating_carForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

class CarForm(forms.ModelForm):
    class Meta:
        model= Car
        fields = '__all__'
