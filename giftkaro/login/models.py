from django.contrib.auth.models import User
import uuid
from django.db import models

class UserData(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=100)

    class Meta():
        db_table = 'LoginData'
    
# class Login(models.Model):
#     username = models.CharField(max_length=100)