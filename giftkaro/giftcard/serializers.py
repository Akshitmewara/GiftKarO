from rest_framework import serializers
from giftcard.models import Giftcard 

class GiftCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Giftcard
        fields = (
                  'giftcard_id',  
                  'name',
                  'img',
                  'disc',)
        