from django.urls import path,include
from .views import *

urlpatterns = [
    path('all/',all),
    path('detail/<int:i>',detail),
    path('shipping/<int:i>',shipping),
    path('delete/',delete),
    path('restore/',restore),
]
