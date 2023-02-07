
from django.urls import path
from . import views

app_name='coupon'

urlpatterns=[
    path('apply/', views.apply_coupon, name='apply_coupon'),
]