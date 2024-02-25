from django.contrib import admin
from .models import Product_Table, product_category
# Register your models here.


admin.site.register(product_category)
admin.site.register(Product_Table)