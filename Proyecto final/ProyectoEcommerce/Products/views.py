from django.shortcuts import render,redirect
from django.http import HttpResponse


from Products.models import Products, Categories
from Products.forms import ProductForm,CategoriesForm

def create_product(request):
    if request.method == 'GET':
        context = {
            'form': ProductForm()
        }

        return render(request, 'products/create-product.html', context=context)

    elif request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            Products.objects.create(
                image=form.cleaned_data['image'],
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
            return render(request, 'products/create-product.html', context=context)

def list_products(request):#diferentes casos de get, si existe alguna busqueda o filtro en particular
    if 'search' in request.GET:
        search = request.GET['search']
        products = Products.objects.filter(name__icontains=search)
    elif 'delete' in request.GET:
        delete = request.GET['delete']
        Products.objects.filter(name=delete).delete()
        products = Products.objects.all()
    elif 'category' in request.GET:
        category = request.GET['category']
        products = Products.objects.filter(category=category)
    else:       
        products = Products.objects.all()
    context={
        "list_of_products": products
    }
    return render (request, 'products/list_prod.html', context=context)


#vista disponible para los superusers- borrar productos
def dashboard_admin(request):
    if 'delete' in request.GET:
        delete = request.GET['delete']
        Products.objects.filter(name=delete).delete()
        products = Products.objects.all()
        categories = Categories.objects.all()   
    elif 'category_to_delete' in request.GET:
        category = request.GET['category_to_delete']
        category_to_del = Categories.objects.filter(name=category)
        category_to_del.delete()
        categories = Categories.objects.all()   
        products = Products.objects.all()
    else:
        products = Products.objects.all()
        categories = Categories.objects.all()   
    context = {
        "list_of_products": products,
        "list_of_categories": categories,

    }
    return render(request, 'dashboard/admin_dashboard.html', context=context)


#vista disponible para los superusers- editar productos
def dashboard_edit(request):
    product_to_edit = request.GET['edit']
    product = Products.objects.filter(name=product_to_edit)
  
    if request.method == 'GET':
        form_update_product = ProductForm(initial={
            'image':product[0].image,
            'name':product[0].name,
            'price': product[0].price,
            'category':product[0].category,
            'stock':product[0].stock,
        })
        context ={
            'form_update_product':form_update_product
        } 
        return render(request, 'dashboard/edit_prod.html', context=context)   
    elif request.method == 'POST':
        form_update_product = ProductForm(request.POST, request.FILES)
        for field in form_update_product:
            print("Field Error:", field.name,  field.errors)
        p = product[0]
        if form_update_product.is_valid():
            p.image = form_update_product.cleaned_data.get('image')
            p.name = form_update_product.cleaned_data.get('name')
            p.price = form_update_product.cleaned_data.get('price')
            p.category = form_update_product.cleaned_data.get('category')
            p.stock = form_update_product.cleaned_data.get('stock')
            p.save()
            return redirect('/Products/list-products/')
        
        context = {
            'errors':form_update_product.errors,
            'form':ProductForm()
        }
        return render(request, 'dashboard/admin_dashboard.html', context=context)  

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
    if 'delete' in request.GET:
        delete = request.GET['delete']
        Categories.objects.filter(name=delete).delete()
        list_of_categories = Categories.objects.all()
    else:
        list_of_categories = Categories.objects.all()
    context={
            "list_of_categories": list_of_categories
    }
    return render (request, 'categories/list-categories.html', context=context)