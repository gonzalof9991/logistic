from django.db import models
from django.contrib.gis.db import models as gis_models

from .order_model import Order
from .base_model import BaseModel


class Client(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    position = gis_models.PointField()

    def __str__(self):
        return f"Client {self.first_name} {self.last_name}"
