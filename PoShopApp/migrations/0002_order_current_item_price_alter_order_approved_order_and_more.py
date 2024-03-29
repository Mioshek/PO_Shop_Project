# Generated by Django 4.0.6 on 2023-01-04 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PoShopApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='current_item_price',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='approved_order',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
