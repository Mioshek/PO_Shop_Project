from django.contrib import admin
from .models import UserProfileInfoModel, Country, AccountType
# Register your models here.
admin.site.register(UserProfileInfoModel)
admin.site.register(Country)
admin.site.register(AccountType)