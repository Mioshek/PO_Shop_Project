from django import forms
from django.core import validators
from django.contrib.auth import get_user_model
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
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"


class UserLogInForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('email', 'password')
        