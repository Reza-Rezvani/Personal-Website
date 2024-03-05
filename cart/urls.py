from django.urls import path,include
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_summery,name='cart_summery'),
    path('add/', views.cart_add,name='cart_add'),
    path('delete/', views.cart_delete,name='cart_delete'),
    path('update/', views.cart_update,name='cart_update'),
]