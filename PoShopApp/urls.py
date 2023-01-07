from django.contrib import admin
from django.urls import path
from . import views

app_name = 'PoShopApp'

urlpatterns = [
    #equipment cbv's
    path('', views.EquipmentListView.as_view(), name="equipment_list"),
    path('equipment/<int:pk>/', views.EquipmentDetailView.as_view(), name='equipment_detail'),
    path('equipment/new/', views.CreateEquipmentView.as_view(), name='equipment_new'),
    path('equipment/<int:pk>/edit/', views.EquipmentUpdateView.as_view(), name='equipment_edit'),
    path('equipment/<int:pk>/remove/', views.EquipmentDeleteView.as_view(), name='equipment_remove'),
    #basket cbv's
    path('basket/', views.BasketListView.as_view(), name='order_list'),
    path('basket/<int:pk>/', views.BasketDetailView.as_view(), name='order_detail'),
    path('basket/<int:pk>/remove/', views.BasketDeleteView.as_view(), name='order_remove'),
    #function based views equipment
    path('equipment/<int:pk>/basket/', views.add_item_to_basket, name='add_item_to_basket'),
    path('basket/<int:pk>/approved', views.approve_order, name='approve_order'),
]

