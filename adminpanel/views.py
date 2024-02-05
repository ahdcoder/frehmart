from django.shortcuts import render
from order.models import Order

def index(request):
    return render(request,"adminpanel/index.html")

def order(request):
    all_orders = Order.objects.all()
    context = {
        'all_order':all_orders
    }
    return render(request,'adminpanel/order/all.html',context)

# Create your views here.
