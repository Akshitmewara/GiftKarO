from rest_framework import serializers
from cart.models import Cards 

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = (
                  'giftcard_id',  
                  'name',
                  'img',
                  'disc',
                  'price',
                  'code',
                  'quantity')
    