from django.urls import path 
from . import views 

urlpatterns = [
    path('view', views.car_list),
    path('',views.cart, name='cart_page'),
    path('cart/update_cart/', views.update_cart_item_quantity, name='update_cart'),
    path('cart/remove_cart_item/', views.remove_cart_item, name='remove_cart_item'),
    path('cart/pay/',views.pay_complete, name='pay'),
]