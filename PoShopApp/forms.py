from socket import fromshare
from django import forms
from django.core import validators
from PoShopApp.models import UserSignIn

class UserSignInForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = UserSignIn
        fields = ('email', 'password')
        
# class UserLogInForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta():
#         model = UserLogin
#         fields = ('email', 'password')
        