from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AccountType(models.Model):
    class PossibleAccountTypeChoice(models.TextChoices):
           CUSTOMER = 'Customer'
           DELIVERYMAN = 'Deliveryman'
           DEALER = 'Dealer'
    account_type = models.CharField(
           max_length=11,
           choices=PossibleAccountTypeChoice.choices,
           default=PossibleAccountTypeChoice.CUSTOMER
    )


class Country(models.Model):
    country = models.CharField(max_length=35, default=None)
    
    def __str__(self) -> str:
         return self.country
    


class UserProfileInfoModel(models.Model, models.TextField):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    flat_num = models.PositiveIntegerField(blank=True, null=True)
    street_number = models.CharField(max_length=5)
    street = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    zip_code = models.PositiveIntegerField()
    phone_number = models.PositiveIntegerField()
    country = models.ForeignKey(Country ,null=True, on_delete=models.SET_NULL)
    
    def __str__(self) -> str:
        return self.user.username
