from django.shortcuts import render
from .models import Blogs_Table
# Create your views here.




def blogs(request):
    all_blogs = Blogs_Table.objects.all()
    context = {'all_blogs':all_blogs}
    return render(request, 'blogs.html', context)

def blog(request):
    return render(request, 'blog.html')




def blog_details(request, slug):
    getBlog = Blogs_Table.objects.get(slug = slug)
    context = {'getBlog':getBlog}
    return render(request, "blog.html", context)