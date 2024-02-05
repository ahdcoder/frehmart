# Generated by Django 4.2.7 on 2024-01-18 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('subcategory', '0003_alter_subcategory_icon_alter_subcategory_status'),
        ('product', '0002_product_category_alter_product_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='category.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='subcategory.subcategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
