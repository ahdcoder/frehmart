from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from .models import Customer

def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_staff:
            return render(request,"adminpanel/index.html")
    else:
        return redirect('/adminpanel/auth_login/')

def customer_all(request):
    all_customer = Customer.objects.all()
    return render(request,'adminpanel/customer_all.html',{'all_customer':all_customer})

# Create your views here.
