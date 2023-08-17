from django.db import models
import uuid

# Create your models here.
class Giftcard(models.Model):
    giftcard_id=models.PositiveIntegerField(primary_key=True,unique=True)
    name=models.CharField(max_length=70)
    img=models.ImageField(upload_to='pics')
    disc=models.TextField()

    class Meta:
        # Mention the collection name here
        # Replace 'custom_collection_name' with your desired collection name
        db_table = 'GiftCard'
