from django.shortcuts import render, redirect
from .models import Digital_Product_Table, Digital_Product_Purchase_Table
# Create your views here.
from django.contrib import messages

def digital_product_page(request):
    active_digital_product = Digital_Product_Table.objects.filter(featured=True)
    context = {'active_digital_product':active_digital_product}
    return render(request, 'digital_product/digital_product_page.html', context)

def digital_product_details(request, slug):
    getdigital_product = Digital_Product_Table.objects.get(slug = slug)
    context = {'getdigital_product':getdigital_product}
    return render(request, 'digital_product/digital_product_details.html', context)


def digital_product_checkout_form_submit(request):
    if request.method == "POST":
        digital_product_id = request.POST.get('digital_product_id')
        Customer_Name = request.POST.get('Customer_Name')
        Customer_Email = request.POST.get('Customer_Email')
        Phone_Number = request.POST.get('Phone_Number')
        print(Customer_Name, Customer_Email, Phone_Number)

        getdigital_product = Digital_Product_Table.objects.get(id=digital_product_id)

        var_digital_product_Checkout_Table = Digital_Product_Purchase_Table(Name=Customer_Name, Email=Customer_Email, Number=Phone_Number, Digital_Product=getdigital_product)
        var_digital_product_Checkout_Table.save()
        messages.success(request, "কিছুক্ষন এর মধ্যে আপনার সাথে আমাদের একজন এজেন্ট যোগাযোগ করবেন। \n জরুরি প্রয়োজনে কল করুন ০১৮২২২২৪০৮০ ")
        # return redirect('digital_product_details', getdigital_product.slug)
        # return render(request, "digital_product/couse_buy_success_page.html")
        # return redirect('https://shop.bkash.com/brainskybd01999147566/pay/bdt1/JYcB8W')
        if getdigital_product.payment_url:
            return redirect(getdigital_product.payment_url)
        else:
            return render(request, "digital_product/digital_product_buy_success_page.html")
    else:
        return redirect('digital_product_page')



def proDentim_product(request):
    return render(request, "digital_product/proDentim_product.html")