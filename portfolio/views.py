from django.shortcuts import render, redirect
from blogs.models import Blogs_Table
from products.models import Product_Table
from .models import Portfolio, contact_form, Portfolio_Category, Newsletter_Table, Pro_Customers
# Create your views here.
from django.contrib import messages
from django.db.models import Q
from django.core.mail import send_mail



def index(request):
    all_product = Product_Table.objects.filter(featured=True).order_by('-id')[:3]
    RECENT_NEWS = Blogs_Table.objects.all().order_by('-id')[:5]
    all_portfolio = Portfolio.objects.all().order_by('-id')[:5]
    pro_customer_list = Pro_Customers.objects.all()
    context = {'RECENT_NEWS':RECENT_NEWS, 'all_product':all_product, 'all_portfolio':all_portfolio, 'pro_customer_list':pro_customer_list}
    return render(request, 'index.html', context)


def search_product(request):
    word = request.GET.get('word')
    filter_products = Product_Table.objects.filter(Q(Name__icontains=word) | Q(tags__icontains=word))
    context = {'filter_products':filter_products}
    return render(request, "search_product.html", context)


def service_AI_and_Machine_Learning(request):
    return render(request, 'service_AI_and_Machine_Learning.html')


def service_Mobile_App_Development(request):
    return render(request, 'service_Mobile_App_Development.html')


def service_Web_Development(request):
    return render(request, 'service_Web_Development.html')


def service_Creative_and_Marketing(request):
    return render(request, 'service_Creative_and_Marketing.html')



def portfolio(request):
    all_portfolio = Portfolio.objects.all()
    all_Portfolio_Category = Portfolio_Category.objects.all()
    context = {
                'all_portfolio':all_portfolio,
               'all_Portfolio_Category':all_Portfolio_Category,
               }
    return render(request, 'portfolio.html', context)


def Newsletter_submit(request):
    ref_url = request.META.get('HTTP_REFERER')
    get_email = request.POST.get('email')

    mail = Newsletter_Table(email=get_email)
    mail.save()
    #
    # all_portfolio = Portfolio.objects.all()
    # all_Portfolio_Category = Portfolio_Category.objects.all()
    # context = {
    #             'all_portfolio':all_portfolio,
    #            'all_Portfolio_Category':all_Portfolio_Category,
    #            }

    send_mail(
        'BrainSkyBD: Subscribe Someone',  # Subject of message
        f'Subscribe Info, Email : {get_email}',  # Message
        'info@brainskybd.com',  # From Email
        [''],  # To Email

        fail_silently=True
    )

    return redirect(ref_url)


def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        var_contact_form = contact_form(name=name, email=email, message=message)
        var_contact_form.save()
        messages.success(request, "Message Sent Successfully !")

        send_mail(
            'Rubytech: Contact Information',  # Subject of message
            f'A user send contact : Name:{name}, Email:{email}, Message : {message}',  # Message
            'info@rubytech.xyz',  # From Email
            ['peyal.nadim@gmail.com'],  # To Email

            fail_silently=True
        )


    return render(request, 'contact.html')

def demo_request(request):
    return render(request, 'demo_request.html')


def Terms_of_use(request):
    return render(request, 'Terms_of_use.html')

def Terms_and_conditions(request):
    return render(request, 'Terms_and_conditions.html')

def Privacy_policy(request):
    return render(request, 'Privacy_policy.html')

def Cookie_policy(request):
    return render(request, 'Cookie_policy.html')

def about_us(request):
    return render(request, 'about_us.html')