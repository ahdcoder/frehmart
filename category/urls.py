from django.contrib import admin
from django.urls import path
from category.views import *

urlpatterns = [
    path('all/',category_all,name='all'),
    path('add/',add_category,name='add'),
    path('delete/',delete,name='delete'),
    path('edit/<int:i>',edit,name='edit'),
]
