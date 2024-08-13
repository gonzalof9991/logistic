from .base_model import BaseModel
from django.db import models


class OrderDetail(BaseModel):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Order Detail {self.order.id} | Product {self.product.name} | Quantity {self.quantity} | Total {self.total}"

    def calculate_total(self):
        self.total = self.product.price * self.quantity
        self.save()
        return self.total

    def calculate_total_order(self):
        order = self.order
        if not order.total:
            order.total = 0
        order.total += self.total
        print(order.total, 'order total')
        print(order.id, 'order id')
        order.save()
