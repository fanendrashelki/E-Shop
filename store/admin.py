from unicodedata import category
from django.contrib import admin

from store.models.customer import Customer
from .models.product import Product
from .models.category import Category
from .models.orders import Order

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']

class AdminCustomer(admin.ModelAdmin):
    list_display=['first_name','last_name','email','phone']




admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Order )