from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# pip install django-braces
# from braces.views import SelectRelatedMixin
# from . import forms
from .models import (Equipment, Order)
from .forms import ShopForm

# #Create your views here.
#EQUIPMENT SECTION
class EquipmentListView(ListView):
    model = Equipment
    
    def get_queryset(self):
        return Equipment.objects.order_by('-category')
    
class EquipmentDetailView(DetailView):
    model=Equipment
    
class CreateEquipmentView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'Shop/equipment_detail.html'
    form_class = ShopForm
    model = Equipment
    
class EquipmentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'Shop/equipment_detail.html'
    form_class = ShopForm
    model = Equipment
    
class EquipmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Equipment
    success_url = reverse_lazy('Shop:order_list')

#BASKET SECTION
class BasketListView(ListView):
    model = Order
    
    def get_queryset(self):
        return Order.objects.order_by('-item')
    
class BasketDetailView(DetailView):
    model=Order
    
    
class BasketDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('Shop:order_list')

## function based views
@login_required
def add_item_to_basket(request, pk):   
    item = get_object_or_404(Equipment, pk=pk)
    basket, created = Order.objects.get_or_create(customer=request.user, item=item)
    basket.add_to_basket()
    return redirect('Shop:equipment_list')

@login_required
def approve_order(request, pk):
    item = get_object_or_404(Order, pk=pk)
    item.approved_order = True
    item.save()
    return redirect('Shop:equipment_list')    
    
