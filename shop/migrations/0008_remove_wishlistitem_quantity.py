# Generated by Django 4.2.7 on 2024-02-07 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_wishlist_wishlistitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistitem',
            name='quantity',
        ),
    ]
