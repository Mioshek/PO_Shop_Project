from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserRegisterForm, UserProfileForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile

# from django.views.generic import 
# Create your views here.

class SignIn(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")
    template_name = "Users/signin.html"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'Users:login'
    signin_url = 'Users:signin'
    redirect_field_name = 'Users:more_info'
    form_class = UserProfileForm
    model = Profile   
