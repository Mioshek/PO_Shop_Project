from django.shortcuts import render
from . import forms
from .forms import UserSignInForm

# Create your views here.

def index(request):
    return render(request, 'PoShopApp/index.html')


def signin_page(request):
    form = UserSignInForm()
    if request.method == "POST":
        form = UserSignInForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else: print("Error form invalid")
    return render(request, 'PoShopApp/signin_page.html', {'form':form})

# def login_page(request):
#     form = UserLogInForm()
#     if request.method == "POST":
#         form = UserLogInForm(request.POST)
        
#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else: print("Error form invalid")
#     return render(request, 'PoShopApp/login.html', {'form':form})

def account_page(request):
    return render(request, 'PoShopApp/account.html')