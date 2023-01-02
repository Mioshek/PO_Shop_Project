# Generated by Django 4.0.6 on 2023-01-02 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PoShopApp', '0003_alter_equipment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='brand',
            field=models.CharField(default='Null', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
    ]
