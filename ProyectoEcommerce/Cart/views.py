from django.shortcuts import render
from Cart.forms import CartForm
from Cart.models import Cart

# Create your views here.
def create_cart(request):
    if request.method == 'GET':
        context = {
            'form': CartForm()
        }

        return render(request, 'cart/cart.html', context=context)
    elif request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            Cart.objects.create( 
            username =  form.cleaned_data['username'],
            products =  form.cleaned_data['products'])
            context = {
                'message': 'Carro creada exitosamente'
            }
            return render(request, 'cart/cart.html',context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': CartForm()
            }
            return render(request, 'cart/cart.html', context=context)

def list_of_carts(request):
    list_of_carts = Cart.objects.all()
    context={
        'list_of_carts':list_of_carts
    }
    return render(request, 'cart/list-of-carts.html', context=context)