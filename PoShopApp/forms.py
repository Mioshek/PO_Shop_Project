from django import forms
from django.core import validators
from .models import Equipment

class ShopForm(forms.ModelForm):
    class Meta():
        model = Equipment
        fields = ('category', 'brand', 'name', 'price')