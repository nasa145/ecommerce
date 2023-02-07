

from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem
from shop.models import Product
from cart.cart import Cart
from .tasks import order_created
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from django.contrib.admin.views.decorators import staff_member_required
from shop.recommender import Recommender

# Create your views here.
def order_checkout(request):
    cart = Cart(request)
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        address = request.POST["address"]
        postal_code = request.POST["postal_code"]
        country = request.POST["country"]
        city = request.POST["city"]
        order_notes = request.POST["order_notes"]

        order = Order(
            first_name = first_name, last_name = last_name, email = email, address = address,
            postal_code = postal_code, country = country, city = city, order_notes = order_notes
        )
        order.save()
        for item in cart:
            OrderItem.objects.create(
                order = order, product = item["product"], price = item["price"], quantity = item["quantity"]
            )
        r = Recommender()
        r.products_bought( [item["product"] for item in cart] )

        cart.clear()
        order_created.delay(order.id)
        return render(request, 'order/order/success.html')

    else:
        return render(request, 'order/order/checkout.html' )



@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string("order/order/pdf.html", {'order':order})
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = f'filename=Order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[
        weasyprint.CSS(settings.STATIC_ROOT + 'assets/css/pdf.css')
    ])
    return response