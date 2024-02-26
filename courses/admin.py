from django.contrib import admin
from .models import Course_Table, course_category, Course_Enrollments_Table
# Register your models here.

admin.site.register(course_category)
admin.site.register(Course_Table)

class show_list_enrollments(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Number', 'Course', 'created', 'updated']
admin.site.register(Course_Enrollments_Table, show_list_enrollments)