from django.db import models

from users.models import User
from goods.models import Products


class OrderitemQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name='User', default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Created Timestamp')
    phone_number = models.CharField(max_length=20, verbose_name='Phone')
    requires_delivery = models.BooleanField(default=False, verbose_name='Requires Delivery')
    delivery_address = models.CharField(blank=True, null=True, verbose_name='Delivery Address')
    payment_on_get = models.BooleanField(default=False, verbose_name='Payment on Get')
    is_paid = models.BooleanField(default=False, verbose_name='Is Paid')
    status = models.CharField(max_length=20, default='In process', verbose_name='Status')

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Order {self.pk} | User {self.user.first_name} {self.user.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='Order')
    product = models.ForeignKey(Products, on_delete=models.SET_DEFAULT, verbose_name='Product',null=True,default=None)
    name = models.CharField(max_length=150, verbose_name='Name')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Price')
    quantity = models.PositiveIntegerField(verbose_name='Quantity',default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Created Timestamp')

    class Meta:
        db_table = 'order_items'
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    objects = OrderitemQueryset.as_manager()

    def products_price(self):
        return round(self.product.total_price() * self.quantity, 2)

    def __str__(self):
        return f"Order {self.order.pk} | Product {self.product.name} | Quantity {self.quantity}"


