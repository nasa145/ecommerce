
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product, NewsletterSubscriber, Brand
from .recommender import Recommender
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.http import require_POST
from django.http import HttpResponse


def product_list(request):
    categories = Category.objects.all()
    categories = categories[:6]
    computers_and_tablets_category = Category.objects.get(name="COMPUTERS & TABLETS")
    gaming_category = Category.objects.get(name="GAMING")
    smartphones_and_mobile_devices_category = Category.objects.get(name="SMARTPHONES & MOBILE DEVICES")
    audio_and_video_category = Category.objects.get(name="AUDIO & VIDEO")
    smart_watches_category = Category.objects.get(name="SMART WATCHES")
    office_and_home_appliances_category = Category.objects.get(name="OFFICE & HOME APPLIANCES")
    products = Product.objects.filter(available=True)
    hot_deal_products = products.filter(sale=True)[:10]
    computers_and_tablets = products.filter(category__name= "COMPUTERS & TABLETS")
    smartphones_and_mobile_devices = products.filter(category__name="SMARTPHONES & MOBILE DEVICES")
    power_and_charging = products.filter(category__name="POWER & CHARGING")
    audio_and_video = products.filter(category__name="AUDIO & VIDEO")
    print(computers_and_tablets_category.name)
    print(categories)
    return render(request,'shop/product/list.html',
                  {'categories': categories,
                  'hot_deal_products':hot_deal_products, 'computers_and_tablets':computers_and_tablets,
                  'smartphones_and_mobile_devices':smartphones_and_mobile_devices,'power_and_charging':power_and_charging,
                  'audio_and_video':audio_and_video,
                  'computers_and_tablets_category':computers_and_tablets_category,
                  'audio_and_video_category':audio_and_video_category,
                  'office_and_home_appliances_category':office_and_home_appliances_category,
                  'smart_watches_category':smart_watches_category,
                  'smartphones_and_mobile_devices_category':smartphones_and_mobile_devices_category,
                  'gaming_category':gaming_category,
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    product_reviews = product.reviews.all()
    r = Recommender()
    suggested_products = r.suggest_products_for([product], 4)
    print(suggested_products)
    return render(request,'shop/product/detail.html',{'product': product, 'product_reviews':product_reviews, 
    "suggested_products":suggested_products})

def categories(request):
    categories = Category.objects.all()
    categories = Category.objects.all()
    tv_category = categories.get(name="TVs")
    brands = Brand.objects.all()
    samsung_brand = brands.get(name="Samsung")
    product_from_each_category = []
    for category in categories:
        product = Product.objects.filter(category=category).first()
        if product != None:
            product_from_each_category.append(product)
    print(tv_category)
    return render(request, 'shop/category/categories.html', {'categories':categories, 
    'products':product_from_each_category, 'brands':brands, 'tv_category':tv_category, 'samsung_brand':samsung_brand } )

def products(request, category_slug=None, brand_slug=None):
    category = None
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    elif brand_slug:
        brand = get_object_or_404(Brand, slug=brand_slug)
        products = products.filter(brand=brand)
    paginator = Paginator(products, 10)
    page = request.GET.get('page') 
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    print(products)
    return render(request, 'shop/product/products.html', {'products':products})



# A views to enable user to subscribe with their emails to the newsleter subscription feature
@require_POST
def newslettersubscription(request):
    email = request.POST.get('subscription-email')
    NewsletterSubscriber.objects.create(email=email)
    return HttpResponse("SUBSCRIBED WELL")

    
    

