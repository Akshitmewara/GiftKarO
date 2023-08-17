from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.giftp, name='home'),
    path("list/", views.gift_card, name="list"),
    path('giftcard/<int:giftcard_id>', views.single_gift_card, name='single_gift_card'),
    path('giftcard/giftcard/add_to_cart/<int:giftcard_id>/<int:price>/', views.add_to_cart, name='add_to_cart'),
]