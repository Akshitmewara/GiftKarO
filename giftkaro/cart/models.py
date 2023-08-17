import uuid
from django.db import models
from login.models import UserData
class Cards(models.Model):
    giftcard_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user=models.CharField(null=True,max_length=80)
    name = models.CharField(max_length=70)
    img = models.ImageField(upload_to='pics')
    disc = models.TextField()
    price = models.PositiveIntegerField(default=0)
    code = models.CharField(max_length=10, unique=True, default=uuid.uuid4, editable=False)
    quantity = models.PositiveIntegerField(default=1)
    razor_pay_order_id = models.CharField(max_length=100,null=True, blank=True)
    date=models.DateField(null=True)
    status= models.BooleanField(default=False)

    
    class Meta:
        # Mention the collection name here
        # Replace 'custom_collection_name' with your desired collection name
        db_table = 'Cart'