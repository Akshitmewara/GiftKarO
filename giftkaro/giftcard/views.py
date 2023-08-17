import json
from sqlite3 import DatabaseError
from django.shortcuts import render
from login.models import UserData
from giftcard.models import Giftcard
from giftcard.serializers import GiftCartSerializer
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from cart.models import Cards


# Create your views here.
def gift_card(request):
    cards = Giftcard.objects.all()
    gift_serializer = GiftCartSerializer(cards,many=True)
    return JsonResponse(gift_serializer.data, safe=False)

from django.shortcuts import render, get_object_or_404,HttpResponse
from .models import Giftcard
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

def add_to_cart(request,giftcard_id, price):
    if request.user.is_authenticated:
        if request.method == 'POST':
            giftcard_id = request.POST.get('giftcard_id')
            price = request.POST.get('price')
            # user = request.user.view
            print(request.user)
            try:
                giftcard = Giftcard.objects.get(pk=giftcard_id)
                
            except Giftcard.DoesNotExist:
                return JsonResponse({'error': 'Gift card not found.'}, status=404)

            try:
                cart_item = Cards.objects.get(
                    user=UserData.username,
                    name=giftcard.name,
                    img=giftcard.img.url,
                    disc=giftcard.disc,
                    price=price,
                )
                print(cart_item)
                print(UserData.user_id)
                return JsonResponse({'error': 'Item already added in Cart.'})
            
            except ObjectDoesNotExist:
                # If the cart item does not exist, create it with get_or_create
                cart_item, created = Cards.objects.get_or_create(
                    user=UserData.user_id,
                    name=giftcard.name,
                    img=giftcard.img.url,
                    disc=giftcard.disc,
                    price=price,
                )
                
            except DatabaseError as e:
            # Log the error and handle it appropriately
                return JsonResponse({'error': 'An error occurred while accessing the database.'}, status=500)

            return JsonResponse({'created': created}, status=200)

        return JsonResponse({'error': 'Invalid request method.'}, status=400)

def homepage_view(request):
    # Your logic for the homepage view goes here
    # For example, you can pass some data to the template and render it
    return render(request, 'gift card/homepage.html')
