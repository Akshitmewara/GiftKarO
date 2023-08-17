from rest_framework import serializers
from login.models import  UserData

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model =  UserData
        fields = ('username',
                  'password',
                  'email',
                  'date_of_birth',
                  'country')