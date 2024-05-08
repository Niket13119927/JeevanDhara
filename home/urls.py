from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signin_p',views.signin_p,name='patient'),
    path('signin_h',views.signin_h,name='hospital'),
    path('signup',views.signup,name='signup'),
    path('signup_p',views.signup_p,name='signup_p'),
    path('signup_h',views.signup_h,name='signup_h'),
    path('bloodtype',views.bloodtype,name='bloodtype'),
    path('hospital',views.hospital),
    path('ambulance',views.ambulance),
    path('about',views.about),
]