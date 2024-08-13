import requests
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import LineString, Point
from django.db import models

from .order_detail import OrderDetail
from .order_model import Order
from .base_model import BaseModel


class Route(BaseModel):
    line = gis_models.LineStringField(null=True, blank=True)
    estimated_time_in_minutes = models.IntegerField(null=True, blank=True)
    total_products = models.IntegerField(null=True, blank=True)
    total_price = models.FloatField(null=True, blank=True)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return f"Route {self.total_products} - {self.total_price}"

    def get_line(self):
        coords = ";".join([f"{order.client.position.x},{order.client.position.y}" for order in self.orders.all()])
        print(coords)
        url = f"http://router.project-osrm.org/route/v1/driving/{coords}?overview=full&geometries=geojson"
        response = requests.get(url)
        data = response.json()
        if data['code'] == 'Ok':
            # Extraer la geometría de la ruta (un array de coordenadas)
            route_geometry = data['routes'][0]['geometry']['coordinates']
            # Convertir a una lista de objetos Point
            puntos = [Point(coord[0], coord[1], srid=4326) for coord in route_geometry]
            # Crear un objeto LineString con los puntos
            self.line = LineString(puntos)
            duration = data['routes'][0]['duration']
            print(duration)
            self.estimated_time_in_minutes = duration / 60
        else:
            raise Exception("Error al obtener la ruta de OSRM")
        # self.line = LineString(coords)

    def get_total_products(self):
        total = 0
        for order in self.orders.all():
            id = order.id
            order_detail: OrderDetail = OrderDetail.objects.filter(order=id)[0]
            if order_detail:
                print(order_detail, 'order_detail')
                total += order_detail.quantity
        self.total_products = total
        return self.total_products

    def get_total_price(self):
        total = 0
        for order in self.orders.all():
            total += order.total
        self.total_price = total
        return self.total_price
