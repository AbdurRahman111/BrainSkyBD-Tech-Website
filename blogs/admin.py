from django.contrib import admin
from .models import blog_category, Blogs_Table
# Register your models here.

admin.site.register(blog_category)

class show_blog_table(admin.ModelAdmin):
    list_display = ['Title', 'Category', 'Author', 'Time']
    readonly_fields = ['total_views', 'Read_Time', 'Time']
admin.site.register(Blogs_Table, show_blog_table)