from django import forms
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm,PasswordResetForm
from django.contrib.auth.models import User
from .models import *

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'name':'username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'name':'first_name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'name':'last_name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'name':'password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'name':'paswword2'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'name':'email'}))

    class Meta:
        model = User
        fields = ['username','password1','password2','email','first_name','last_name']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'name':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'name':'password'}))

# class OrderForm(forms.ModelForm):

#     p = [
#         ('Cash','Cash'),
#         ('on the Credit','on the Credit'),
#     ]

#     first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     payment_type = forms.CharField(widget=forms.RadioSelect(attrs={'class':'form-control','font-size':'width:10px','name':'1'},choices=p))
#     address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','font-size':'width:10px','name':'2'}))
#     phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    

#     class Meta:
#         model = Order
#         fields = ['first_name','last_name','address','payment_type','phone_number']

