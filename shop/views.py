from django.shortcuts import render
from .models import Product

# Create your views here.
def index_view(request):
    all_products = Product.objects.all()
    return render(request, 'store/index.html', {'products': all_products})


def product_view(request,pid):
    product = Product.objects.get(id=pid)
    return render(request, 'store/product.html', {'product': product})


