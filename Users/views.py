from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from PoShopApp.models import Order
from django.views.generic import CreateView

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# from django.views.generic import 
# Create your views here.

# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('index'))

# @login_required
# def account_page(request, pk):
#     order = get_object_or_404(Order, pk=pk)
#     return redirect('account', pk=order.pk)

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 return HttpResponse("ACCOUNT NOT ACTIVE")
#         else: 
#             print("Someone tried to login and failed!")
#             print("Username: {} and password {}".format(username, password))
#             return HttpResponse("invalid login details supplied!")
#     else:
#         return render(request, 'Users/login.html', {})


class SignUp(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")
    template_name = "Users/signup.html"

# def user_sign_in(request):
#     registered:bool = False
#     if request.method == 'POST':
#         user = UserRegisterForm(data=request.POST)
#         if user.is_valid():
#             user=user.save()
#             user.set_password(user.password)
#             user.save()
            
#             if 'profile_pic' in request.FILES:
#                 user.profile_pic = request.FILES['profile_pic']
                
#             user.save()
#             registered = True
            
#         else:
#             print(user.errors)
            
#     else:
#         user = UserRegisterForm()
        
#     return render(request, 'Users/signin.html',
#                   {'user':user,
#                     'registered': registered})
    
    
