from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('shop',views.shop,name='shop'),
    path('blog',views.blog,name='blog'),
    path('about',views.about,name='about'),
    path('cart',views.view_cart,name='cart'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('product_details/<int:id>/',views.product_details),
    path('add_to_cart/<int:item_id>/<int:item_quantity>/<int:price>/',views.add_to_cart),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)