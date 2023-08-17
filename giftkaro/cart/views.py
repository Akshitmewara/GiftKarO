import datetime
from decimal import Decimal
from bson import Decimal128
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from cart.models import Cards
from rest_framework.parsers import JSONParser
from rest_framework import status 
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import razorpay
from cart.serializers import CardSerializer
from django.conf import settings

# Create your views here.
@api_view(['GET'])
def car_list(request):
    request.method == 'GET'
    carts = Cards.objects.all()
    card_serializer = CardSerializer(carts,many=True)
    return JsonResponse(card_serializer.data, safe=False)
    
def cart(request):
    carts = Cards.objects.all()
    total = 0
    print(carts)
    cart_item_count = Cards.objects.count()
    # if request.method == 'POST':
    for cart in carts:
        price = cart.price 
        total += price
    val = total * 100
    if total > 0:
        client = razorpay.Client(auth = (settings.KEY, settings.SECRET))
        payment = client.order.create({'amount': val, 'currency': 'INR', 'payment_capture': 1})
        context = {'cart' : val, 'payment': payment}
        test = 0
        if payment['id'] is not None:
            for cart in carts:
                cart.razor_pay_order_id = payment['id']
                cart.save()
                cart.status = True
                cart.save()
                cart.date = datetime.date.today()
                cart.save()
        #     new_order = orders_m.objects.create(date=card.date,img=card.img,price=card.price,giftcard_id=card.giftcard_id,code=card.code)
        # new_order.save()
        
        return render(request, 'cart/cart.html', {'carts': carts, 'total': total, 'payment': payment, 'cart_item_count': cart_item_count})
    else:
        return render(request, 'cart/cart.html', {'carts': carts, 'total': total, 'cart_item_count': cart_item_count})

    # Calculate subtotal, tax, and total
    # subtotal = sum(cart.price for cart in carts)
    # tax = subtotal * 0.07  # Assuming 7% tax, you can adjust this value as needed
    # total = subtotal + tax
    # Cards.razor_pay_order_id = payment['id']
    # Cards.save()
    # return render(request, 'cart/cart.html', {'carts': carts, 'total': total, 'payment': payment,'show_total': show_total})

from django.shortcuts import redirect

from django.shortcuts import render, redirect, get_object_or_404
from .models import Cards
@csrf_exempt 
def remove_cart_item(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        try:
            cart = Cards.objects.get(pk=cart_id)
            cart.delete()
        except Cards.DoesNotExist:
            return JsonResponse({'error': 'Cart item not found.'})
    carts = Cards.objects.all()
    return render(request, 'cart/cart.html', {'carts': carts})

@csrf_exempt  # Disabling CSRF protection for simplicity. Use proper CSRF protection in production.
def update_cart_item_quantity(request):
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id')
        new_quantity = int(request.POST.get('new_quantity'))
        new_price = int(request.POST.get('new_price'))

        try:
            cart_item = Cards.objects.get(pk=cart_item_id)
            if new_quantity > 0:
                cart_item.quantity = new_quantity
                cart_item.save()
                cart_item.price = new_price
                cart_item.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'error': 'Invalid quantity.'})
        except Cards.DoesNotExist:
            return JsonResponse({'error': 'Cart item not found.'})

    return JsonResponse({'error': 'Invalid request.'})

def pay_complete(request):
    carts = Cards.objects.all()
    return render(request,'cart/pay.html',{'carts':carts})
