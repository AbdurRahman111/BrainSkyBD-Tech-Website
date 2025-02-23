from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import digital_product_category, Digital_Product_Table, Digital_Product_Purchase_Table
# Register your models here.

admin.site.register(Digital_Product_Table)
admin.site.register(digital_product_category)

class show_list_enrollments(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Number', 'Digital_Product', 'created', 'updated']
admin.site.register(Digital_Product_Purchase_Table, show_list_enrollments)