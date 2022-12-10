from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Equipment(models.Model):
    category_name = models.CharField(max_length=64)
    brand = models.CharField(max_length=64)
    
    def __str__(self) -> str:
        return self.category_name
    pass

class Fishing_rod(models.Model): 
    rod_id = models.ForeignKey(Equipment,
                                on_delete=models.CASCADE,
                                related_name='fishing_rods')
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(10000)])
    
    def __str__(self) -> str:
        return self.name
    
class Spinning_wheel(models.Model):
    spinnig_wheel_id = models.ForeignKey(Equipment,
                                on_delete=models.CASCADE,
                                related_name='spinning_wheels')
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def __str__(self) -> str:
        return self.name
class Chair(models.Model):
    chair_id = models.ForeignKey(Equipment,
                                on_delete=models.CASCADE,
                                related_name='chairs')
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def __str__(self) -> str:
        return self.name
class Natural_bait(models.Model):
    bait_id = models.ForeignKey(Equipment,
                                on_delete=models.CASCADE,
                                related_name='natural_baits')
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def __str__(self) -> str:
        return self.name
class Crankbait(models.Model):
    crankbait_id = models.ForeignKey(Equipment,
                                on_delete=models.CASCADE,
                                related_name='crankbaits')
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def __str__(self) -> str:
        return self.name
class Twister(models.Model):
    twister_id = models.ForeignKey(Equipment,
                                on_delete=models.CASCADE,
                                related_name='twisters')
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def __str__(self) -> str:
        return self.name
class Rubber_bait(models.Model):
    rubber_bait_id = models.ForeignKey(Equipment,
                                on_delete=models.CASCADE,
                                related_name='rubber_baits')
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def __str__(self) -> str:
        return self.name
