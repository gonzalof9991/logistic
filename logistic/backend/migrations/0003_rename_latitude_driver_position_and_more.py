# Generated by Django 5.0.7 on 2024-08-07 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_driver_email_driver_first_name_driver_last_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='latitude',
            new_name='position',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='longitude',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]