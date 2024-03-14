from django.db import models


class CartQuerySet(models.QuerySet):
    def total_price(self):
        return sum([cart.products_price() for cart in self])

    def total_quantity(self):
        if self:
            return sum([cart.quantity for cart in self])
        return 0


class Cart(models.Model):
    user = models.ForeignKey(to="users.User", on_delete=models.CASCADE, verbose_name="User", blank=True, null=True)
    product = models.ForeignKey(to="goods.Products", on_delete=models.CASCADE, verbose_name="Product")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Quantity")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Created Timestamp")
    session_key = models.CharField(max_length=40, verbose_name="Session Key", blank=True, null=True)

    class Meta:
        db_table = "cart"
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    objects = CartQuerySet().as_manager()

    def products_price(self):
        return round(self.product.total_price() * self.quantity, 2)

    def __str__(self):
        if self.user:
            return f'Cart {self.user.username} | Item {self.product.name} | Quantity {self.quantity}'
        return f'Anonim Cart {self.session_key} | Item {self.product.name} | Quantity {self.quantity}'
