from django import forms
from django.core import validators
from django.contrib.auth.models import User
from Users.models import UserProfileInfoModel, AccountType

class UserBasicForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta():
        model = User
        fields = ('username','email', 'password')


class UserAccountTypeForm(forms.ModelForm):
    class Meta():
        model = AccountType
        fields = ('account_type',)


class UserAdvancedForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfoModel
        fields = ('first_name',
                'last_name', 
                'profile_pic',
                'flat_num',
                'street_number',
                'street',
                'city',
                'zip_code',
                'phone_number',
                'country')


class UserLogInForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('email', 'password')
        