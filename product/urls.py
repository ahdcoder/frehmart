from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('all/',all),
    path('add/',add),
    path('edit/<int:i>',edit),
    path('delete/',delete),
    path('detail/<int:i>',detail)
]
