
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='account'

urlpatterns=[
    #custom urls for signup and login
    path('signup', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    #USE THE DJANGO BUILT AUTHENTICATION URLS TO ALLOW USERS TO WORK WITH THEIR ACCOUMTS
    
    #PASSWORDS RESET FOR PEOPLE WHO FORGOT PASSWORDS
    path('reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/Done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #Enable the users to change their passwords
    path('passsword_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]