from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.


class UserProfileInfoModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    
    class PossibleAccountTypeChoice(models.TextChoices):
        CUSTOMER = 'Customer'
        DELIVERYMAN = 'Deliveryman'
        DEALER = 'Dealer'
    account_type = models.CharField(
        max_length=11,
        choices=PossibleAccountTypeChoice.choices,
        default=PossibleAccountTypeChoice.CUSTOMER
    )
    
    def __str__(self) -> str:
        return self.user.username


class Equipment(models.Model):
    category_name = models.CharField(max_length=64)
    brand = models.CharField(max_length=64)
    
    def __str__(self) -> str:
        return self.category_name
    pass

class Fishing_rod: 
    rod_id = models.ForeignKey(Equipment,
                                on_delete=models.CASCADE,
                                related_name='fishing_rods')
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(10000)])
    
    def __str__(self) -> str:
        return self.name
    
class Spinning_wheel:
    spinnig_wheel_id = models.ForeignKey(Equipment,
                                on_delete=models.CASCADE,
                                related_name='spinning_wheels')
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def __str__(self) -> str:
        return self.name
class Chair:
    chair_id = models.ForeignKey(Equipment,
                                on_delete=models.CASCADE,
                                related_name='chairs')
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def __str__(self) -> str:
        return self.name
class Natural_bait:
    bait_id = models.ForeignKey(Equipment,
                                on_delete=models.CASCADE,
                                related_name='natural_baits')
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def __str__(self) -> str:
        return self.name
class Crankbait:
    crankbait_id = models.ForeignKey(Equipment,
                                on_delete=models.CASCADE,
                                related_name='crankbaits')
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def __str__(self) -> str:
        return self.name
class Twister:
    twister_id = models.ForeignKey(Equipment,
                                on_delete=models.CASCADE,
                                related_name='twisters')
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def __str__(self) -> str:
        return self.name
class Rubber_bait:
    rubber_bait_id = models.ForeignKey(Equipment,
                                on_delete=models.CASCADE,
                                related_name='rubber_baits')
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                        MaxValueValidator(1000)])
    
    def __str__(self) -> str:
        return self.name
