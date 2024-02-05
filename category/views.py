from django.shortcuts import render,redirect
from category.models import *
from .forms import *
from django.http import JsonResponse

def category_all(request):
    category_form = CategoryForm
    all_category = Category.objects.all()

    context = {
        'category_form':category_form,
        'all_category':all_category
    }
    return render(request,'adminpanel/category/all_category.html',context)

def add_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')

        new_category = Category.objects.create(name=category_name)

        data = f'<tr id="category_{new_category.id}", style="color: rgb(190, 178, 178);">' \
               f'<td>{new_category.name}</td>' \
               f'<td>{new_category.create_at}</td>' \
               f'<td>{new_category.update_at}</td>' \
               f'<td> <div class="form-button-action"> <button type="button" data-toggle="tooltip" title="" class="btn btn-link btn-primary btn-lg" data-original-title="Edit Task"><i class="fa fa-edit"></i></button><button type="button"  onclick="deleteCategory({new_category.id})" data-toggle="tooltip" title="" class="btn btn-link btn-danger" data-original-title="Remove"><i class="fa fa-times"></i></button></div></td>'\
               f'</tr>'
        return JsonResponse(data,safe=False)
    
    return JsonResponse({},status=400)

def delete(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        category.delete()

        return JsonResponse({},status=200)
    return JsonResponse({},status=400)

def edit(request,i):
    s_category = Category.objects.get(id=i)
    form = CategoryForm(instance=s_category)
    if request.method == 'POST':
        category = CategoryForm(request.POST,instance=s_category).save()
        return redirect('/adminpanel/category/all/')
    context = {
        'category_form':form,
        's_category':s_category
    }
    return render(request,'adminpanel/category/edit_category.html',context)

# Create your views here.
