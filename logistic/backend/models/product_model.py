from django.db import models

from .base_model import BaseModel


class Product(BaseModel):
    sku = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    price = models.FloatField(default=0)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"Product {self.name}"
