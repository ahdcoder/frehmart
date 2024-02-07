from django.contrib import admin
from django.urls import path,include
from adminpanel.views import *

urlpatterns = [
    path('',index),
    path('category/',include('category.urls')),
    path('subcategory/',include('subcategory.urls')),
    path('product/',include('product.urls')),
    path('order/',include('order.urls')),
    path('auth_admin/',include('auth_admin.urls')),
    path('customer_all/',customer_all)
]
