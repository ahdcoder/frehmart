from django.urls import path,include
from .views import *

urlpatterns = [
    path('auth_login/',auth_login),
    path('auth_logout/',auth_logout),
    path('worker_add/',worker_add),
    path('worker_all/',worker_all),
    path('worker_edit/<int:i>',worker_edit),
    path('worker_delete/',worker_delete),

]
