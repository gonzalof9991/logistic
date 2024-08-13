# Generated by Django 5.0.7 on 2024-08-09 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_ordermodel_productmodel_vehiclemodel_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientModel',
            new_name='Client',
        ),
        migrations.RenameModel(
            old_name='OrderModel',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='ProductModel',
            new_name='Product',
        ),
        migrations.RenameModel(
            old_name='RouteModel',
            new_name='Route',
        ),
        migrations.RenameModel(
            old_name='VehicleModel',
            new_name='Vehicle',
        ),
    ]