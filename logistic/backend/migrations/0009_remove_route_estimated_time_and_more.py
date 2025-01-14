# Generated by Django 5.0.7 on 2024-08-12 22:01

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_remove_route_destination_remove_route_origin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='estimated_time',
        ),
        migrations.AddField(
            model_name='route',
            name='estimated_time_in_minutes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='line',
            field=django.contrib.gis.db.models.fields.LineStringField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='route',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='total_products',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
