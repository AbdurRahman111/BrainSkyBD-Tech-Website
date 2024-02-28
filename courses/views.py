from django.shortcuts import render, redirect
from .models import Course_Table, Course_Enrollments_Table
# Create your views here.
from django.contrib import messages

def course_page(request):
    active_course = Course_Table.objects.filter(featured=True)
    context = {'active_course':active_course}
    return render(request, 'courses/course_page.html', context)

def course_details(request, slug):
    getCourse = Course_Table.objects.get(slug = slug)
    context = {'getCourse':getCourse}
    return render(request, 'courses/course_details.html', context)


def checkout_form_submit(request):
    if request.method == "POST":
        course_id = request.POST.get('course_id')
        Customer_Name = request.POST.get('Customer_Name')
        Customer_Email = request.POST.get('Customer_Email')
        Phone_Number = request.POST.get('Phone_Number')
        print(Customer_Name, Customer_Email, Phone_Number)

        getCourse = Course_Table.objects.get(id=course_id)

        var_Course_Checkout_Table = Course_Enrollments_Table(Name=Customer_Name, Email=Customer_Email, Number=Phone_Number, Course=getCourse)
        var_Course_Checkout_Table.save()
        messages.success(request, "কিছুক্ষন এর মধ্যে আপনার সাথে আমাদের একজন এজেন্ট যোগাযোগ করবেন। \n জরুরি প্রয়োজনে কল করুন ০১৮২২২২৪০৮০ ")
        # return redirect('course_details', getCourse.slug)
        # return render(request, "courses/couse_buy_success_page.html")
        return redirect('https://shop.bkash.com/brainskybd01999147566/pay/bdt1/JYcB8W')
    else:
        return redirect('course_page')