from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from Users.models import Profile
# Create your models here.


class EquipmentCategories(models.TextChoices):
    FISHING_ROD = 'Fishing Rod'
    SPINNING_WHEEL = 'Spinning Wheel'
    CHAIR = 'Chair'
    NATURAL_BAIT = 'Natural Bait'
    CRANKBAIT = 'Crankbait'
    TWISTER = 'Twister'
    RUBBER_BAIT = 'Rubber Bait'
    WOBBLERS = 'Wobblers'
  
class Equipment(models.Model):
        
    category = models.CharField(
           max_length=50,
           choices=EquipmentCategories.choices
    )
    brand = models.CharField(max_length=64, null=True, default='Null')
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def get_absolute_url(self):
        return reverse("shop_list", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return self.name
    

class Order(models.Model):
    customer = models.ForeignKey(Profile, null=True, on_delete=models.PROTECT)
    total_price = models.PositiveIntegerField(null=True)
    orderdate = models.DateTimeField(blank=True, null=True)
    approved_order = models.BooleanField(default=False)
    basket = models.ForeignKey('PoShopApp.Equipment', related_name='basket_items', on_delete=models.CASCADE, null=True)
    
    def get_absolute_url(self):
        return reverse("shop_list", kwargs={"pk": self.pk})
    
    def add_to_basket(self):
        self.total_price = timezone.now()
    
    def approve_orders(self):
        self.save()
        return self.filter(approved_order=True)
    
    def __str__(self) -> str:
        return self.customer.user.username
    