from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Coupon
from django.utils import timezone
from django.views.decorators.http import require_POST

# Create your views here.
@require_POST
def apply_coupon(request):
    try:
        coupon_code = request.POST.get('coupon_code', None)
        coupon = Coupon.objects.get(code=coupon_code, active=True,
            valid_from__gte=timezone.now(), valid_to__lte=timezone.now()
        )
        request.session['coupon_id'] = coupon.id
        print(coupon.code)
    except Coupon.DoesNotExist:
        request.session['coupon_id'] = None
        print('NOTHING WORKS HERE FOR NOW')
    return redirect('cart:cart_detail')
    

        