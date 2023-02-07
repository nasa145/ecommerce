from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.db import IntegrityError

# Create your views here.

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.add_message(request, messages.ERROR, 'Password Do not match')
            return render(request, 'registration/login.html' )
        else:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                messages.add_message(request, messages.SUCCESS, 'You have Successfully Signed up, You can now login into your account and purchase products with a nice discount')
                return redirect('shop:product_list')
            except IntegrityError:
                messages.add_message(request, messages.ERROR, 'The chosen username or email already exists')
                return render(request, 'registration/login.html' )
    else:
        return render(request, 'registration/login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                next_url = request.POST.get('next','/')
                return redirect(next_url)
            else:
                messages.add_message(request, messages.ERROR, 'Disabled Account')
                return render(request, 'registration/login.html')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid email or password')
            return render(request, 'registration/login.html')
    else:
        next_url = request.GET.get('next','/')
        return render(request, 'registration/login.html', {'next':next_url})

def logout_view(request):
    logout(request)
    return redirect('account:login')

