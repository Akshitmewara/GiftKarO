from rest_framework import serializers
from order.models import  orders_m

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model =  orders_m
        fields = (
                  'orderid',
                  'img',
                  'status',
                  'date',
                  'name',
                  'price',)