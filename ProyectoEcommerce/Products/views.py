from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
from Products.models import Products, Categories
from Products.forms import ProductForm,CategoriesForm

def create_product(request):
    if request.method == 'GET':
        context = {
            'form': ProductForm()
        }

        return render(request, 'products/create-product.html', context=context)

    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            Products.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                category=form.cleaned_data['category'],
                stock=form.cleaned_data['stock'],
            )
            context = {
                'message': 'Producto creado exitosamente'
            }
            return render(request, 'products/create-product.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': ProductForm()
            }
            return render(request, 'products/create_product.html', context=context)

def list_products(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = Products.objects.filter(name__icontains=search)
    elif 'category' in request.GET:
        category = request.GET['category']
        products = Products.objects.filter(category=category)
    else:
        products = Products.objects.all()
    context={
        "list_of_products": products
    }
    return render (request, 'products/list_prod.html', context=context)

def create_category(request):
    if request.method == 'GET':
        context = {
            'form': CategoriesForm()
        }

        return render(request, 'categories/create-categories.html', context=context)
    elif request.method == 'POST':
        form = CategoriesForm(request.POST)
        if form.is_valid():
            Categories.objects.create( name =  form.cleaned_data['name'])
           
            return redirect('/Products/list-categories/')
        else:
            context = {
                'form_errors': form.errors,
                'form': ProductForm()
            }
            return render(request, 'products/create_product.html', context=context)

def list_categories(request):
    if 'search' in request.GET:
        search = request.GET['search']
        list_of_categories = Categories.objects.filter(name__icontains=search)
    else:
        list_of_categories = Categories.objects.all()
    context={
            "list_of_categories": list_of_categories
    }
    return render (request, 'categories/list-categories.html', context=context)