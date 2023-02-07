
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('categories/', views.categories, name='categories'),
    path('products/', views.products, name='products'),
    path('<slug:category_slug>/', views.products, name='products_by_category'),

    #Query or get products by their brands
    path('<slug:brand_slug>/products/', views.products, name='products_by_brand'),
    
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('newsletter/subscriotion/', views.newslettersubscription, name='newsletersubscription'),
]