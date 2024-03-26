from django import template
from shop.models import Product
from shop.models import Category

register = template.Library()

@register.inclusion_tag('store/category_summery.html')
def productcategories():
    product = Product.objects.all()
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=product.filter(category=name).count
    return {'categories':cat_dict}