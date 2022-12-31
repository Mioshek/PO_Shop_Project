from django.contrib import admin
from django.urls import path
from . import views

app_name = 'PoShopApp'

urlpatterns = [
    path('shop/', views.show_shop, name='show_shop'),
    path('order/<int:pk>', views.order, name='order'),
]

