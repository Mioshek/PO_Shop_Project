from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Country(models.Model):
    country = models.CharField(max_length=35, default=None)
    
    def __str__(self) -> str:
         return self.country
     
     
class AccountType(models.TextChoices):
    CUSTOMER = 'Customer'
    DELIVERYMAN = 'Deliveryman'
    SALESMAN = 'Salesman'
    
     
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    account_type = models.CharField(max_length=50, choices=AccountType.choices, default=AccountType.CUSTOMER)
    flat_num = models.PositiveIntegerField(blank=True, null=True)
    street_number = models.CharField(max_length=5)
    street = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    zip_code = models.PositiveIntegerField()
    phone_number = models.PositiveIntegerField(blank=True, unique=True, null=True)
    country = models.ForeignKey(Country ,null=True, on_delete=models.PROTECT)
    
    def get_absolute_url(self):
        return reverse("signin", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return self.user.email

    
    
