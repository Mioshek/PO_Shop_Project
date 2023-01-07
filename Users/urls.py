from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Users'

urlpatterns = [
    path('signup/', views.SignIn.as_view(), name='signin'),
    path('login/', auth_views.LoginView.as_view(template_name="Users/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('more/<int:pk>/', views.ProfileUpdateView.as_view(), name='more_info'),
    # path('account/<int:pk>', views.account_page, name='account'),
]