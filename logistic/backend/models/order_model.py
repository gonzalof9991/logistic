from django.db import models
from django.contrib.gis.db import models as gis_models
from .base_model import BaseModel


class Order(BaseModel):
    position = gis_models.PointField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    payment_method = models.CharField(max_length=50, null=True, blank=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Order {self.id} | {self.client.first_name} {self.client.last_name} | {self.total}"
