from django.db import models

from .base_model import BaseModel


class Vehicle(BaseModel):
    name = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=50, unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.license_plate}"
