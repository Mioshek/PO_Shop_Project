from django.shortcuts import render
from . import forms
from . import models

# Create your views here.

def index(request):
    return render(request, 'PoShopApp/index.html')

def shop(request):
    context_dict = {'Equipment':models.Equipment}
    return render(request, 'basic_app/index.html', context_dict)

