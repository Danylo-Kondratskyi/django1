from django.contrib import admin
from goods.models import Category, Products


# Register your models here.

# admin.site.register(Category)
# admin.site.register(Products)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fields = [
        'name',
        'slug',
        'category',
        'description',
        ('price', 'discount'),
        'quantity',
        'image'
    ]
    list_display = ['name', 'price', 'quantity', 'discount']
    list_editable = ['price', 'discount', 'quantity']
    search_fields = ['name', 'description']
    list_filter = ['category']

