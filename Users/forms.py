from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Users.models import Profile

ACCOUNT_TYPES=(
    ("1","CUSTOMER"),
    ("2","DELIVERYMAN"),
    ("3","SALESMAN"),
    )


class UserProfileForm(forms.ModelForm):
    class Meta():
        account_type = forms.ChoiceField(choices=ACCOUNT_TYPES)
        model = Profile
        fields = ("user", "account_type",
                  "flat_num","street_number",
                  "street","city","zip_code",
                  "phone_number","country")
        

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user


class UserLogInForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('email', 'password')
        