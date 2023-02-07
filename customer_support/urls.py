
from django.urls import path
from . import views

app_name='customer_support'

urlpatterns=[
    #information urls
    path('about_us/', views.about_us, name='about_us'),
    path('faq', views.faq, name='faq'),
    path('shopping/', views.how_to_shop, name='how_to_shop'),
    path('contact_us/', views.contact_us, name='contact_us'),
    
    #customer service urls
    path('returns/', views.returns, name='returns'),
    path('help/', views.help, name='help'),
    path('payment/', views.payment_methods, name='payment_methods'),
    path('guarantee/', views.money_back_guarantee, name='money_back_guarantee'),
    path('shipping/', views.shipping, name='shipping'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]