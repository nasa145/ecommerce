# Generated by Django 4.1.3 on 2023-01-26 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand_products', to='shop.brand'),
        ),
    ]
