from django.contrib import admin
from django.urls import path,include,reverse_lazy
from .views import *
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


urlpatterns = [ 
    path('',index),
    path('category/<int:i>',category),
    path('category_2/<int:i>',category_2),
    path('user_register/',user_register),
    path('logout/',logout_),
    path('user_login/',user_login),
    path('confirm_acc/',confirm_acc),
    path('addcart/<int:i>',addcart),
    path('product_cart/',product_cart),
    path('cart_delete/<int:i>',cart_delete),
    path('product_delete/<int:i>',product_delete),
    path('checkout/',checkout),
    path('add_comment_pro/',add_comment_proo),
    path('product_detail/<int:i>',product_detail),
    path('comment_delete/',comment_delete),
    path('search/',search),
    path('password-reset/',PasswordResetView.as_view(template_name='shop/users/password_reset_form.html',email_template_name='shop/users/password_reset_email.html',success_url=reverse_lazy('password_reset_done')),name='password_reset'),
    path('password-reset/done/',PasswordResetDoneView.as_view(template_name='shop/users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='shop/users/password_reset_confirm.html',success_url=reverse_lazy('password_reset_complate')),name='password_reset_confirm'),
    path('password-reset/complate/',PasswordResetCompleteView.as_view(template_name='shop/users/password_reset_complete.html'),name='password_reset_complate')

]