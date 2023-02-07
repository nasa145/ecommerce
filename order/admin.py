from django.contrib import admin
from .models import Order, OrderItem
from django.utils.safestring import mark_safe
from django.urls import reverse

# Register your models here.
class OrderItemAdmin(admin.TabularInline):
    model = OrderItem

def order_pdf(obj):
    url = reverse('order:admin_order_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}">PDF</a>')
order_pdf.short_description = 'Invoice'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 'last_name', 'email', 'address','postal_code', 'city', 'created','updated', 'paid',
        order_pdf
    ]
    list_filter = ['created', 'updated', 'paid']
    inlines = [OrderItemAdmin, ]
