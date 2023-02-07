from django.shortcuts import render

# Create your views here.

#The views concerned with the informatio folder and templates that give information about the comapny

def about_us(request):
    return render(request, 'information/about_us.html')

def contact_us(request):
    return render(request, 'information/contact_us.html')

def faq(request):
    return render(request, 'information/faq.html')

def how_to_shop(request):
    return render(request, 'information/how_to_shop.html')



#The views that direct the user to customer services and render the templates

def returns(request):
    return render(request, 'customer_services/returns.html')

def money_back_guarantee(request):
    return render(request, 'customer_services/money_back_guarantee.html')

def payment_methods(request):
    return render(request, 'customer_services/payment_methods.html')

def privacy_policy(request):
    return render(request, 'customer_services/privacy_policy.html')

def shipping(request):
    return render(request, 'customer_services/shipping.html')

def terms_and_conditions(request):
    return render(request, 'customer_services/terms_and_conditions.html')

def help(request):
    return render(request, 'customer_services/help.html')