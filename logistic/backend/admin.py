from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Vehicle, Driver, Route, Client, Product, Order, OrderDetail

# Register your models here.
admin.site.register(Vehicle)

admin.site.register(Product)


@admin.register(OrderDetail)
class OrderDetailModelAdmin(LeafletGeoAdmin):
    change_form_template = 'admin/backend/change_form.html'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.calculate_total()
        obj.calculate_total_order()
        # calculate total of order
        obj.save()


@admin.register(Order)
class OrderModelAdmin(LeafletGeoAdmin):
    change_form_template = 'admin/backend/change_form.html'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.save()


@admin.register(Route)
class RouteAdmin(LeafletGeoAdmin):
    change_form_template = 'admin/backend/change_form.html'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.get_line()
        obj.get_total_products()
        obj.get_total_price()
        obj.save()


@admin.register(Client)
class ClientAdmin(LeafletGeoAdmin):
    change_form_template = 'admin/backend/change_form.html'


@admin.register(Driver)
class DriverAdmin(LeafletGeoAdmin):
    change_form_template = 'admin/backend/change_form.html'
