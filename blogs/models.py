from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
import readtime
from django.utils.text import slugify


class blog_category(models.Model):
    class Meta:
        verbose_name_plural = 'Blog Category'
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Blogs_Table(models.Model):
    class Meta:
        verbose_name_plural = 'Blog Table'
    Title = models.CharField(max_length=255)
    slug = models.SlugField(default="Auto-Generate", editable=False)
    Category = models.ForeignKey(blog_category, on_delete=models.CASCADE)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='Blog_images/', blank=True, null=True)
    Short_Description = models.TextField(default="", blank=True, null=True)
    Description = RichTextField(blank=True, null=True)
    tags = models.CharField(max_length=255, default="", blank=True, null=True)
    Read_Time = models.CharField(max_length=255, default="", blank=True, null=True)
    total_views = models.IntegerField(default=0, null=True, blank=True)
    Time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.Title


    def save(self, *args, **kwargs):
        # result = readtime.of_text(self.Description)
        result = readtime.of_html(self.Description)
        self.Read_Time = result.text

        # make random order ID
        my_slug = slugify(self.Title)
        uniqe_confirm = Blogs_Table.objects.filter(slug=my_slug)
        count_num = 0
        while uniqe_confirm:
            count_num = count_num + 1
            my_slug = str(slugify(self.Title))+ "-" + str(count_num)
            if not Blogs_Table.objects.filter(slug=my_slug):
                break
        if self.slug == "Auto-Generate":
            self.slug = my_slug
        else:
            pass
        super(Blogs_Table, self).save(*args, **kwargs)



