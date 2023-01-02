from django.contrib import admin
from django.urls import path
from . import views

app_name = 'PoShopApp'

urlpatterns = [
    path('', views.EquipmentListView.as_view(), name="shop_list"),
    path('item/new/', views.CreateEquipmentView.as_view(), name='shop_new'),
    path('item/<int:pk>/edit/', views.EquipmentUpdateView.as_view(), name='shop_edit'),
]

