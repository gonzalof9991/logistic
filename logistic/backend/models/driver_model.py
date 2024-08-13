from django.db import models
from django.contrib.gis.db import models as gis_models

from .base_model import BaseModel
from .route_model import Route
from .vehicle_model import Vehicle


class Driver(BaseModel):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, unique=True, null=True)
    password = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    hired_date = models.DateField()
    position = gis_models.PointField(null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    routes = models.ManyToManyField(Route)

    def __str__(self):
        return self.username
