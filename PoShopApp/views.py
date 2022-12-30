from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView,)

from django.views import generic

# pip install django-braces
# from braces.views import SelectRelatedMixin
# from . import forms
from .models import (Fishing_rod,Spinning_wheel,
                      Chair,Natural_bait,Crankbait,
                      Twister,Rubber_bait, Order)


# #Create your views here.
# class EquipmentList(SelectRelatedMixin, generic.ListView):
#     model = Fishing_rod,Spinning_wheel,Chair,Natural_bait,Crankbait,Twister,Rubber_bait
#     select_related = ("", "price")
    
def show_shop(request):
    fishing_rod = Fishing_rod.objects.all()
    spinning_wheel = Spinning_wheel.objects.all()
    chair = Chair.objects.all()
    natural_bait = Natural_bait.objects.all()
    crankbait = Crankbait.objects.all()
    twister = Twister.objects.all()
    rubber_bait = Rubber_bait.objects.all()
    return render(request,"PoShopApp/testshop.html", {"fr":fishing_rod,
                                                   "sw":spinning_wheel,
                                                   "c":chair,
                                                   "nb":natural_bait,
                                                   "cb":crankbait,
                                                   "t":twister,
                                                   "rb":rubber_bait})
    
