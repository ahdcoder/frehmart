from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Customer

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form__input','placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form__input','placeholder':'Password'}))

class CustomerForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'YOUR NAME'}),required=False)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'SUBJECT'}),required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':10,'placeholder':'MESSAGE'}),required=False)
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter Your Email'}))

    class Meta:
        model = Customer
        fields = ['email','subject','message']