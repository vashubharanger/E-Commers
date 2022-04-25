from django.contrib import admin

# Register your models here.

from .models import Product, Contact, Order, Orders, OrderUpdate

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
