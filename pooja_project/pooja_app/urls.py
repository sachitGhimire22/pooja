from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('shop',views.shop,name='shop'),
    path('blog',views.blog,name='blog'),
    path('about',views.about,name='about'),
    path('cart',views.cart,name='cart'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    
]