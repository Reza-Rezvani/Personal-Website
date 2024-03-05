from django.urls import path,include
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index_view,name='index'),
    path('product/<int:pid>', views.product_view, name='product'),
]