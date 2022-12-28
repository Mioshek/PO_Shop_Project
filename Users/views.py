from django.shortcuts import render
from .forms import UserRegisterForm

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# from django.views.generic import 
# Create your views here.

def index(request):
    return render(request, 'PoShopApp/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def account_page(request):
    return render(request, 'Users/account.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('account'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else: 
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'Users/login.html', {})

def user_sign_in(request):
    registered:bool = False
    if request.method == 'POST':
        user = UserRegisterForm(data=request.POST)
        if user.is_valid():
            user=user.save()
            user.set_password(user.password)
            user.save()
            
            if 'profile_pic' in request.FILES:
                user.profile_pic = request.FILES['profile_pic']
                
            user.save()
            registered = True
            
        else:
            print(user.errors)
            
    else:
        user = UserRegisterForm()
        
    return render(request, 'Users/signin.html',
                  {'user':user,
                    'registered': registered})
