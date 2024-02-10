from django.db import models
from category.models import *

class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category_of_subcategory',blank=True,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    icon = models.ImageField(upload_to="subcategory/",blank=True,null=True)
    status = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name

# Create your models here.
