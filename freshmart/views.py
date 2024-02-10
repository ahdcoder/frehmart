from django.shortcuts import render
from django.http import Http404
from requests import Response
from rest_framework.views import APIView
from rest_framework import generics
from category.models import Category
from subcategory.models import Subcategory
from product.models import Product
from .serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser,IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdminOrReadOnly
from rest_framework.pagination import PageNumberPagination


def error_404(request):
    return render(request,'404.html')

class CategoryAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CategoryAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = CategoryAPIListPagination
    permission_classes = (IsAdminOrReadOnly,) #dine admin (is_staff)


class CategoryAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsAuthenticated,) dine registratiya edenler ucin
    permission_classes = (IsAdminOrReadOnly,) #dine admin (is_staff)

    # authentication_classes = (TokenAuthentication,)

class CategoryAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,) #dine admin (is_staff)


    # SubcategoryAPI
class SubcategoryAPIListPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 1000

class SubcategoryAPIList(generics.ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = (IsAdminUser,)
    pagination_class = SubcategoryAPIListPagination

class SubcategoryAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = (IsAdminUser,)

class SubcategoryAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = (IsAdminUser,)


    # ProductAPI

class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # OrderAPI

class OrderAPIList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    



