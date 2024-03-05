from django.db import models
import datetime



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=500, blank=True, null=True, default='')
    price = models.DecimalField(default=0, decimal_places=0, max_digits=12)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    picture = models.ImageField(upload_to='upload/product/')
    # is_sale = models.BooleanField(default=False)
    # sale_price = models.DecimalField(default=0, decimal_places=0, max_digits=12)

    
    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(blank=True, default='', max_length=400)
    phone = models.CharField(blank=True, max_length=20)
    date = models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)



    def __str__(self):
        return self.product