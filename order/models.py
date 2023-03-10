from django.db import models
from shop.models import Product

# Create your models here.
class Order(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15, default='e.g 2547 1234 5678')
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, default="Your nation/state/country")
    city = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    order_notes = models.TextField(blank=True, null=True, default="order notes")
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id}"

    class Meta:
        ordering = ['-created',]

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity