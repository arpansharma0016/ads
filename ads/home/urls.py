from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('referred_register/<str:ref>/', views.referred_register, name='referred_register'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('confirm_email/<str:uname>/', views.confirm_email, name='confirm_email'),
    path('resend_code/<str:uname>/', views.resend_code, name='resend_code'),
    path('referred_confirm_email/<str:uname>/<str:ref>/', views.referred_confirm_email, name='referred_confirm_email'),
    path('referred_resend_code/<str:uname>/<str:ref>/', views.referred_resend_code, name='referred_resend_code'),
    path('enter_otp/<str:uname>/', views.enter_otp, name='enter_otp'),
    path('enter_otp/', views.forgot_password, name='forgot_password'),
    path('new_password/<str:uname>/', views.new_password, name='new_password'),
    path('resend_pass_code/<str:uname>/', views.resend_pass_code, name='resend_pass_code'),
    path('logout/', views.logout, name='logout'),
    path('', views.home, name="home"),
]
