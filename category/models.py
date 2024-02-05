from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name
    


# Create your models here.
