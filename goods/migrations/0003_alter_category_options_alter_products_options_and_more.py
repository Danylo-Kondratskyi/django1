# Generated by Django 5.0.2 on 2024-03-02 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("goods", "0002_alter_category_options_alter_category_table_products"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="products",
            options={
                "ordering": ("id",),
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                max_length=100, unique=True, verbose_name="Category Name"
            ),
        ),
        migrations.AlterField(
            model_name="products",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="goods.category",
                verbose_name="Categories",
            ),
        ),
    ]
