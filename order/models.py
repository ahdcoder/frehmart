from django.db import models
from shop.models import Cart

class Order(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    payment_type = models.CharField(max_length=55)
    address = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    cart = models.OneToOneField(Cart,on_delete=models.CASCADE,related_name='order')
    phone_number = models.CharField(max_length=15)
    status = models.IntegerField(default=0)
    

# Create your models here.
