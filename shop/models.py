from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class ConfirmCode(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='confirmcode')
    pincode = models.CharField(max_length=30)
    email = models.EmailField(max_length=255)
    status = models.BooleanField(default=False)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='carts')
    status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    

    def totalsum(self):
        full_price = 0
        for i in self.items.all():
            full_price += i.total_price()
            
        return full_price
    
    def delivery(self):
        if self.totalsum() > 100:
            return '0'
        else:
            return '10'
        
    def full_total_sum(self):
        price = 0
        for i in self.items.all():
            price += i.total_price()
        price += int(self.delivery())
        return price 
        

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name = 'products')
    quantity = models.SmallIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.quantity * self.product.new_price
    

class Wishlist(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='wishlist')
    create_at = models.DateTimeField(auto_now_add=True)

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist,on_delete=models.CASCADE,related_name='wishlistitem')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product')
    create_at = models.DateTimeField(auto_now_add=True)

# class Order(models.Model):
#     first_name = models.CharField(max_length=55)
#     last_name = models.CharField(max_length=55)
#     payment_type = models.CharField(max_length=55)
#     address = models.CharField(max_length=255)
#     create_at = models.DateTimeField(auto_now_add=True)
#     cart = models.OneToOneField(Cart,on_delete=models.CASCADE,related_name='order')
#     phone_number = models.CharField(max_length=15)





# Create your models here.
