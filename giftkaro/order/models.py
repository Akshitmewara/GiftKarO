from django.db import models



# Create your models here.
class orders_m(models.Model):
    giftcard_id=models.IntegerField()
    img=models.ImageField(upload_to='pics')
    date=models.DateField(max_length=10)
    # name=models.CharField(max_length=70)
    price=models.FloatField(max_length=20)
    code=models.CharField(max_length=80)
    status=models.CharField(max_length=20)
    
    class Meta():      
        db_table='order'
        
        
        
