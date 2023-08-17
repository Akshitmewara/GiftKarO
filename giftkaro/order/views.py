import json
from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from cart.models import Cards
from order.models import  orders_m
from rest_framework.parsers import JSONParser
from rest_framework import status 
from rest_framework.decorators import api_view


from order.serializers import orderSerializer 
from django.views import View


# @api_view(['GET'])
# def orderp(request):
#     request.method == 'GET'
#     orders = orders_m.objects.all()
    # order_serializer = orderSerializer(orders,many=True)
#     return JsonResponse(order_serializer.data, safe=False)
# for fecth data to model in json response


@api_view(['GET'])
def giftp(request):
    gift = Giftcard.objects.all()
    cart_item_count = Cards.objects.count()
    gift_serializer = GiftCartSerializer(gift,many=True)
    return render(request,'Home/home.html',{'gifts': gift, 'cart_item_count': cart_item_count,})

# def cart_item_count(request):
#     # Calculate the number of items in the cart
#     count = Cards.objects.count()
#      # Render the template and pass the cart item count as context
#     return render(request, 'Home/home.html', {'cart_item_count': count})

def single_gift_card(request, giftcard_id):
    giftcard = get_object_or_404(Giftcard, pk=giftcard_id)
    cart_item_count = Cards.objects.count()
    return render(request, 'gift card/Giftcart.html', {"giftcard": giftcard, 'cart_item_count': cart_item_count,})

from giftcard.models import Giftcard
from cart.models import Cards
# Import the CartItem model (assuming you have one)
import pdb; 
from django.core.exceptions import ObjectDoesNotExist

def add_to_order(request,giftcard_id, price):
    cards_to_order = Cards.objects.filter(status=True)
    for card in cards_to_order:
        new_order = orders_m.objects.create(date=card.date,img=card.img,price=card.price,giftcard_id=card.giftcard_id,code=card.code)
        new_order.save()
        print(card)

    
    return JsonResponse({'message': 'Cards added to order successfully.'})



@api_view(['GET'])
def orderp(request):
    orders = orders_m.objects.all()
    list = []
    carts = Cards.objects.all()
    cart_item_count = Cards.objects.count()
    for cart in carts:
        if cart.status == True:
            list.append(cart)
            
    return render(request,'order page/orderpage.html',{'cart': list,'cart_item_count': cart_item_count})
    
    order_serializer = orderSerializer(orders,many=True)
    
    
   



   


class OrderHistoryView(View):
    def get(self, request, giftcard_id):
        # Get a specific order from the database using the order_id
        print("Order ID in OrderHistoryView:", giftcard_id)  # Add this line to check the value of order_id
          # Get a specific order from the database using the order_id
        cart = orders_m.objects.get(giftcard_id=giftcard_id)
        return render(request, 'orderhistory.html', {'cart': cart})
    
    