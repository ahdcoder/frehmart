from django.contrib import admin
from django.urls import path
from subcategory.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('all/',all),
    path('delete/',delete),
    path('save/',save),
    path('edit/<int:i>',edit),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
