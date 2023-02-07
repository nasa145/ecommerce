
from celery import shared_task
from django.core.mail import EmailMessage
from .models import Order
from io import BytesIO
import weasyprint
from django.template.loader import render_to_string
from django.conf import settings


@shared_task
def order_created(order_id):
   order = Order.objects.get(id=order_id)
   html_string = render_to_string("order/order/pdf.html", { "order":order })
   output = BytesIO()
   html = weasyprint.HTML(string=html_string)
   pdf = html.write_pdf(output, stylesheets=[
    weasyprint.CSS(settings.STATIC_ROOT+'assets/css/pdf.css')
   ])

   subject = f'My Shop - EE Invoice no. {order.id}'
   message = 'Please, find attached the invoice for your recent purchase'

   email = EmailMessage(
        subject,
        message,
        'appsnasa57@gmail.com',
        [order.email],
        reply_to=['appsnasa57@gmail.com'],
   )
   email.attach('invoice', output.getvalue(), 'application/pdf')
   email.send()
   return email