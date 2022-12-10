from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models
from cities_light.models import Region, City
from smart_selects.db_fields import ChainedForeignKey
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


class UserProfileInfoModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    address_1 = models.CharField(_("address"), max_length=128)
    address_2 = models.CharField(_("additional address"), max_length=128, blank=True)
    city = ChainedForeignKey(City, chained_field="state", chained_model_field="region")
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    zip_code = models.CharField(_("zip code"), max_length=5, default="00000")
    
    
    def __str__(self) -> str:
        return self.user.username
