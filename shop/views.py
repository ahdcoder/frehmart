from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import JsonResponse
from category.models import Category
from subcategory.models import Subcategory
from product.models import Product,Comment
from product.forms import CommentForm
from shop.forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
import random
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from order.models import Order
from order.forms import OrderForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models.functions import Lower


def index(request):
    category = Category.objects.filter(status=2)
    category_status0 = Category.objects.filter(status=0)
    subcategory = Subcategory.objects.all()
    context = {
        'all_categories':category,
        'subategory':subcategory,
        'category':category_status0
    }
    return render(request,'shop/index.html',context)

filter_price = [
    {'val':'0','name':'Price','id':'1'},
    {'val':'1','name':'Under $25','id':'2'},
    {'val':'2','name':'$25 to 50','id':'3'},
    {'val':'3','name':'$50 to 100','id':'3'},
    {'val':'4','name':'$100 to 200','id':'4'},
    
]

filter_sort = [
    {'val':'0','name':'Sort By'},
    {'val':'1','name':'Price: Lowest first'},
    {'val':'2','name':'Price: Highest first'},
    {'val':'3','name':'Product Name: A to Z'},
    {'val':'4','name':'Product Name: Z to A'},
]

def category(request,i):
    obj = Subcategory.objects.get(id=i)
    category = Category.objects.filter(status=2)
    category_status0 = Category.objects.filter(status=0)
    s_pro = Product.objects.filter(subcategory=obj)
    filter_price_id = request.GET.get('filter_price')
    filter_sort_id = request.GET.get('filter_sort')

    usualy_filter = s_pro
    if filter_price_id == '0':
        usualy_filter = s_pro.filter(new_price__gte=0)

    if filter_price_id == '1':
        usualy_filter = s_pro.filter(new_price__lte=24).order_by('new_price')

    if filter_price_id == '2':
        usualy_filter = s_pro.filter(new_price__gte=24,new_price__lte=51).order_by('new_price')

    if filter_price_id == '3':
        usualy_filter = s_pro.filter(new_price__gte=49,new_price__lte=101).order_by('new_price')

    if filter_price_id == '4':
        usualy_filter = s_pro.filter(new_price__gte=99,new_price__lte=201).order_by('new_price')

    # SORT FILTER

    if filter_sort_id == '0':
        usualy_filter
    if filter_sort_id == '1':
        usualy_filter = s_pro.order_by('new_price')

    if filter_sort_id == '2':
        usualy_filter = s_pro.order_by('-new_price')
    
    if filter_sort_id == '3':
        usualy_filter = s_pro.order_by(Lower('name'))

    if filter_sort_id == '4':
        usualy_filter = s_pro.order_by(Lower('name')).reverse()

    paginator = Paginator(usualy_filter,2)
    page_number = request.GET.get('page')

    try:
        usualy_filter_finish = paginator.page(page_number)
    except PageNotAnInteger:
        usualy_filter_finish = paginator.page(1)
    except EmptyPage:
        usualy_filter_finish = paginator.page(paginator.num_pages)


    context = {
        'all_subs':usualy_filter_finish,
        'filter_price_value':filter_price,
        'filter_price_id':filter_price_id,
        'filter_sort_value':filter_sort,
        'paginator_page_id':page_number,
        'filter_sort_id':filter_sort_id,
        'category':category_status0,
        'all_categories':category,
    }
    return render(request,'shop/category.html',context)

symbols = ['%','$','=','@']

def category_2(request,i):
    obj = Category.objects.get(id=i)
    s_pro = Product.objects.filter(category=obj)
    category = Category.objects.filter(status=2)
    category_status0 = Category.objects.filter(status=0).exclude(id=obj.id)
    filter_price_id = request.GET.get('filter_price')
    filter_sort_id = request.GET.get('filter_sort')

    usualy_filter = s_pro
    if filter_price_id == '0':
        usualy_filter = s_pro.filter(new_price__gte=0)

    if filter_price_id == '1':
        usualy_filter = s_pro.filter(new_price__lte=24).order_by('new_price')

    if filter_price_id == '2':
        usualy_filter = s_pro.filter(new_price__gte=24,new_price__lte=51).order_by('new_price')

    if filter_price_id == '3':
        usualy_filter = s_pro.filter(new_price__gte=49,new_price__lte=101).order_by('new_price')

    if filter_price_id == '4':
        usualy_filter = s_pro.filter(new_price__gte=99,new_price__lte=201).order_by('new_price')

    # SORT FILTER

    if filter_sort_id == '0':
        usualy_filter
    if filter_sort_id == '1':
        usualy_filter = s_pro.order_by('new_price')

    if filter_sort_id == '2':
        usualy_filter = s_pro.order_by('-new_price')
    
    if filter_sort_id == '3':
        usualy_filter = s_pro.order_by(Lower('name'))

    if filter_sort_id == '4':
        usualy_filter = s_pro.order_by(Lower('name')).reverse()

    paginator = Paginator(usualy_filter,2)
    page_number = request.GET.get('page')

    try:
        usualy_filter_finish = paginator.page(page_number)
    except PageNotAnInteger:
        usualy_filter_finish = paginator.page(1)
    except EmptyPage:
        usualy_filter_finish = paginator.page(paginator.num_pages)


    context = {
        'all_subs':usualy_filter_finish,
        'filter_price_value':filter_price,
        'filter_price_id':filter_price_id,
        'filter_sort_value':filter_sort,
        'paginator_page_id':page_number,
        'filter_sort_id':filter_sort_id,
        'category':category_status0,
        'all_categories':category,
    }
    return render(request,'shop/category_2.html',context)

def random_generator(number):
    password = ''
    for i in range(number):
        step = random.randint(1,3)
        if step == 1:
            password += str(random.randint(1,9))
        if step == 2:
            password += chr(random.randint(65,90))
        if step == 3:
            password += random.choice(symbols)

    return password

def send_message_to_customer(user,pincode):
    subject = "Welcome to We online shop"
    message = f'''Hi, Thankyou for register
                Your username: {user.username}
                ActiveCode: {pincode}'''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject,message,email_from,recipient_list)

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        errors = False
        if (password1 != password2):
            messages.error(request,'Invalid is Password')
            errors = True

        if User.objects.filter(username=username):
            messages.error(request,'Invalid is Username')
            errors = True

        if User.objects.filter(email=email):
            messages.error(request,'Email is authorized')
            errors = True
        form = RegisterForm(request.POST)

        if form.is_valid() and errors == False:
            user = form.save()
            pincode = random_generator(6)
            email = request.POST['email']
            ConfirmCode.objects.create(user=user,pincode=pincode,email=email)
            send_message_to_customer(user,pincode)
            
            login(request,user)
            return redirect('/confirm_acc/')

    form = RegisterForm()
    context = {
        'form':form
    }
    return render(request,'shop/users/user_register.html',context)


        
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        username = request.POST['username']
        

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            
        if not User.objects.filter(username=username):
            messages.error(request,'Invalid username or password')
        else:
            messages.error(request,'Invalid username or password')
            
    form = LoginForm()
    context = {
        'form':form
    }
    return render(request,'shop/users/user_login.html',context)

def confirm_acc(request):
    if request.method == 'POST':
        if request.user.confirmcode.pincode == request.POST['confirmcode']:
            user = request.user.confirmcode
            user.status = 1
            user.save()
            return redirect('/')

    return render(request,'shop/users/user_confirm.html')

    

def logout_(request):
    logout(request)
    return redirect('/')


def addcart(request,i):
    if request.user.is_authenticated:
        product = Product.objects.get(id=i)
        cart,created = Cart.objects.get_or_create(user=request.user,status=False)
        cartitem,created = CartItem.objects.get_or_create(cart=cart,product=product)
        cartitem.quantity += 1
        cartitem.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    else:
        return redirect('/shop/user_login/')
    
def product_delete(request,i):
    if request.user.is_authenticated:
        product = Product.objects.get(id=i)
        cart,created = Cart.objects.get_or_create(user=request.user,status=False)
        cartitem,created = CartItem.objects.get_or_create(product=product,cart=cart)
        if cartitem.quantity > 0:
            cartitem.quantity -= 1
        cartitem.save()
        if cartitem.quantity == 0:
            cartitem.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    else:
        return redirect('/user_login/')
    
def cart_delete(request,i):
    if request.user.is_authenticated:
        product = Product.objects.get(id=i)
        cart,created = Cart.objects.get_or_create(user=request.user,status=False)
        cartitem,created = CartItem.objects.get_or_create(cart=cart,product=product)
        cartitem.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    else:
        return redirect('/user_login/')
    
def product_cart(request):
    return render(request,'shop/product_cart.html')

def checkout(request):
    form = OrderForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            order = form.save(commit=False)
            cart = request.user.carts.filter(status=False)[0]
            order.cart = cart
            cart.status = True
            cart.save()
            order.save()
            return redirect('/')
        
    context = {
        'form':form
    }
    return render(request,'shop/checkout.html',context)
    

def product_detail(request,i):

    select_product = Product.objects.get(id=i)
    new_product = Product.objects.all()[0:10]
    comment = Comment.objects.filter(product=select_product)
    form_comment = CommentForm()

    
    context = {
        'product':select_product,
        'products':new_product,
        'form':form_comment,
        'comment':comment
    }

    return render(request,'shop/product_detail.html',context)

def add_comment_proo(request):
    if request.method == 'POST':
        comment_name = request.POST.get('comment_name')
        
        product_id = request.POST.get('product_id')
        print(product_id,comment_name)
        s_pro = Product.objects.get(id=product_id)

        comment = Comment.objects.create(user=request.user,comment=comment_name,product=s_pro)

        data = f'''<div id='comment_{comment.id}'>
                <div class="comment-meta">
                <span class="author">{request.user.username}</span> - <span class="time">{comment.create_at}</span> 
                <button type="button" onclick="deleteComment({comment.id})" >  Delete</button></div>
				<div class="comment-content">{comment_name}</div></div>'''

       
        
        return JsonResponse(data,safe=False)
    
def comment_delete(request):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return JsonResponse({},status = 200)
    else:
        return JsonResponse({},status=400)
    
def search(request):
    search_name = request.GET['search_name']

    category = Category.objects.filter(status=2)
    category_status0 = Category.objects.filter(status=0)
    s_pro = Product.objects.filter(name__contains=search_name)
    filter_price_id = request.GET.get('filter_price')
    filter_sort_id = request.GET.get('filter_sort')

    usualy_filter = s_pro
    if filter_price_id == '0':
        usualy_filter = s_pro.filter(new_price__gte=0)

    if filter_price_id == '1':
        usualy_filter = s_pro.filter(new_price__lte=24).order_by('new_price')

    if filter_price_id == '2':
        usualy_filter = s_pro.filter(new_price__gte=24,new_price__lte=51).order_by('new_price')

    if filter_price_id == '3':
        usualy_filter = s_pro.filter(new_price__gte=49,new_price__lte=101).order_by('new_price')

    if filter_price_id == '4':
        usualy_filter = s_pro.filter(new_price__gte=99,new_price__lte=201).order_by('new_price')

    # SORT FILTER

    if filter_sort_id == '0':
        usualy_filter
    if filter_sort_id == '1':
        usualy_filter = s_pro.order_by('new_price')

    if filter_sort_id == '2':
        usualy_filter = s_pro.order_by('-new_price')
    
    if filter_sort_id == '3':
        usualy_filter = s_pro.order_by(Lower('name'))

    if filter_sort_id == '4':
        usualy_filter = s_pro.order_by(Lower('name')).reverse()

    paginator = Paginator(usualy_filter,2)
    page_number = request.GET.get('page')

    try:
        usualy_filter_finish = paginator.page(page_number)
    except PageNotAnInteger:
        usualy_filter_finish = paginator.page(1)
    except EmptyPage:
        usualy_filter_finish = paginator.page(paginator.num_pages)


    context = {
        'all_subs':usualy_filter_finish,
        'filter_price_value':filter_price,
        'filter_price_id':filter_price_id,
        'filter_sort_value':filter_sort,
        'paginator_page_id':page_number,
        'filter_sort_id':filter_sort_id,
        'category':category_status0,
        'all_categories':category,
        'search_name':search_name
    }

    
    return render(request,'shop/serach_product.html',context)
# Create your views here.
