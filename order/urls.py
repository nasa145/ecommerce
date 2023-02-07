
from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.order_checkout, name='order_checkout'),
    path('admin/order/<int:order_id>/pdf/', views.admin_order_pdf, name='admin_order_pdf'),
]