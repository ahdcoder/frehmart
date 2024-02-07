from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='customer')
    name = models.CharField(max_length=33,blank=True,null=True)
    subject = models.CharField(max_length=33,blank=True,null=True)
    message = models.CharField(max_length=255,blank=True,null=True)
    email = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
