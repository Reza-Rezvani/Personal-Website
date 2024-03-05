from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from shop.models import Product
from django.http import JsonResponse


def cart_summery(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    return render(request, 'carts/cart_summery.html', {'cart_products': cart_products})


def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)

        cart_quantity = cart.__len__()

        response = JsonResponse({'qty': cart_quantity})
        return response



def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response = JsonResponse({'product': product_id})
        return response



def cart_update(request):
    pass
