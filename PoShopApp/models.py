from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Fishing_rod(models.Model): 
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(10000)])
    
    def __str__(self) -> str:
        return self.name
    
class Spinning_wheel(models.Model):
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def __str__(self) -> str:
        return self.name
class Chair(models.Model):
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def __str__(self) -> str:
        return self.name
class Natural_bait(models.Model):
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def __str__(self) -> str:
        return self.name
class Crankbait(models.Model):
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def __str__(self) -> str:
        return self.name
class Twister(models.Model):
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def __str__(self) -> str:
        return self.name
class Rubber_bait(models.Model):
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def __str__(self) -> str:
        return self.name
    
    
class Equipment(models.Model):
    class EquipmentCategories(models.TextChoices):
        FISHING_ROD = Fishing_rod
        SPINNING_WHEEL = Spinning_wheel
        CHAIR = Chair
        NATURAL_BAIT = Natural_bait
        CRANKBAIT = Crankbait
        TWISTER = Twister
        RUBBER_BAIT = Rubber_bait
        
    category_name = models.CharField(
           max_length=50,
           choices=EquipmentCategories.choices
    )
    brand = models.CharField(max_length=64)
    
    def __str__(self) -> str:
        return self.category_name
