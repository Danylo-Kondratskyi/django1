from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category Name", unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    image = models.ImageField(upload_to='products_images', blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    discount = models.DecimalField(default=0, verbose_name='Discount', max_digits=7, decimal_places=2)
    quantity = models.IntegerField(default=0, verbose_name='Quantity')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Categories')

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('id',)

    def __str__(self):
        return f'{self.name} Quantity: {self.quantity} Price: {self.price}'

    def display_id(self):
        return f'{self.id:05}'

    def total_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
