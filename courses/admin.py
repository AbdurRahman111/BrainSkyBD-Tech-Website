from django.contrib import admin
from .models import Course_Table, course_category, Course_Checkout_Table
# Register your models here.

admin.site.register(course_category)
admin.site.register(Course_Table)

class show_list_checkout(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Number', 'Course', 'created', 'updated']
admin.site.register(Course_Checkout_Table)