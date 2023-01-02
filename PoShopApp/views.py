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
# class EquipmentList(SelectRelatedMixin, generic.ListView):
#     model = Fishing_rod,Spinning_wheel,Chair,Natural_bait,Crankbait,Twister,Rubber_bait
#     select_related = ("", "price")
class EquipmentListView(ListView):
    model = Equipment
    
    def get_queryset(self):
        return Equipment.objects.order_by('-category')
    
class CreateEquipmentView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'shop/equipment_detail.html'
    from_class = ShopForm
    model = Equipment
    
class EquipmentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'shop/equipment_detail.html'
    from_class = ShopForm
    model = Equipment
    
class EquipmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Equipment
    success_url = reverse_lazy('equipment_list')
    

## function based views
   
@login_required
def order(request, pk):
    item = get_object_or_404(Order, pk=pk)
    item.add_to_cart()
    return redirect('testshop',pk=pk)    
    
