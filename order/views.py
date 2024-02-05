from django.shortcuts import render,HttpResponseRedirect
from django.http import JsonResponse
from .models import Order

def all(request):
    all_orders = Order.objects.all().exclude(status=2)
    context = {
        'all_orders':all_orders,
    }
    return render(request,'adminpanel/order/all.html',context)

def detail(request,i):
    s_order = Order.objects.get(id=i)
    context = {
        'order':s_order
    }
    return render(request,'adminpanel/order/detail.html',context)

def shipping(request,i):
    order = Order.objects.get(id=i)
    if order.status == 0:
        order.status = 1
        order.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    if order.status == 1:
        order.status = 0
        order.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def delete(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
        order.status = 2
        order.save()

        return JsonResponse({},status=200)
    else:
        return JsonResponse({},status=400)
    
def restore(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
        order.status = 0
        order.save()
        JsonResponse({},status=200)
    restore_order = Order.objects.filter(status=2)
    context = {
        'order':restore_order
    }
    return render(request,'adminpanel/order/restore.html',context)

    

# Create your views here.
