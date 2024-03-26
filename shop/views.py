from django.shortcuts import render
from .models import Product

# Create your views here.
def index_view(request, **kwargs):
    all_products = Product.objects.all()
    if kwargs.get('cat_name') != None:
        all_products = all_products.filter(category__name=kwargs['cat_name'])
    return render(request, 'store/index.html', {'products': all_products})


def product_view(request,pid):
    product = Product.objects.get(id=pid)
    return render(request, 'store/product.html', {'product': product})



def category_summary(request, cat_name):
    all_products = Product.objects.all()
    product = all_products.filter(category__name=cat_name)
    return render(request, 'store/index.html', {'product': product})



