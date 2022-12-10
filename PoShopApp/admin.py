from django.contrib import admin
from .models import (Equipment,
                    Fishing_rod,
                    Spinning_wheel,
                    Chair,
                    Natural_bait,
                    Crankbait,
                    Twister,
                    Rubber_bait)

# Register your models here.
admin.site.register(Equipment)
admin.site.register(Fishing_rod)
admin.site.register(Spinning_wheel)
admin.site.register(Chair)
admin.site.register(Natural_bait)
admin.site.register(Crankbait)
admin.site.register(Twister)
admin.site.register(Rubber_bait)