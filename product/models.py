from django.db import models
from category.models import *
from subcategory.models import *
from django.contrib.auth.models import User
class Product(models.Model):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE,related_name='products',blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products',blank=True,null=True)
    new_price = models.DecimalField(max_digits=5, decimal_places=2)
    old_price = models.DecimalField(max_digits=5, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    comment = models.CharField(max_length=100)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='product_comment')
    create_at = models.DateTimeField(auto_now_add = True)





# Create your models here.
