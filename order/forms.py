from django import forms
from .models import Order

class OrderForm(forms.ModelForm):

    p = [
        ('Cash','Cash'),
        ('on the Credit','on the Credit'),
    ]

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    payment_type = forms.CharField(widget=forms.RadioSelect(attrs={'class':'form-control','font-size':'width:10px','name':'1'},choices=p))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','font-size':'width:10px','name':'2'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = Order
        fields = ['first_name','last_name','address','payment_type','phone_number']
