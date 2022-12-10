from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signin/', views.user_sign_in, name='signin'),
    path('login/', views.user_login, name='login'),
    path('account/', views.account_page, name='account'),
    path('chaining/', include('smart_selects.urls')),
]