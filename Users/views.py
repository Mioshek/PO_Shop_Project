from django.shortcuts import render
from .forms import UserBasicForm, UserAdvancedForm, UserAccountTypeForm

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
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
        user_basic = UserBasicForm(data=request.POST)
        user_advanced = UserAdvancedForm(data=request.POST)
        account_type = UserAccountTypeForm(data=request.POST)
        
        if user_basic.is_valid() and user_advanced.is_valid():
            user=user_basic.save()
            user.set_password(user.password)
            user.save()
            
            profile = user_advanced.save(commit=False)
            profile.user = user
            
            user_type = account_type.save()
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                
            profile.save()
            registered = True
            
        else:
            print(user_basic.errors, user_advanced.errors, account_type.errors)
            
    else:
        user_basic = UserBasicForm()
        user_advanced = UserAdvancedForm()
        account_type = UserAccountTypeForm()
        
    return render(request, 'Users/signin.html',
                  {'user_basic':user_basic,
                   'user_advanced':user_advanced,
                   'account_type':account_type,
                    'registered': registered})
