from rest_framework import serializers
from category.models import Category
from subcategory.models import Subcategory
from product.models import Product
from order.models import Order

class CategorySerializer(serializers.ModelSerializer):
    # status = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = Category
        fields = '__all__'

class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'