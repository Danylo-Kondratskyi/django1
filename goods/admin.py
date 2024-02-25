from django.contrib import admin
from goods.models import Category, Products

# Register your models here.

# admin.site.register(Category)
# admin.site.register(Products)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
