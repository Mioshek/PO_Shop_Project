# Generated by Django 4.0.6 on 2023-01-04 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PoShopApp', '0003_rename_basket_order_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
    ]
