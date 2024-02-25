from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
import readtime
from django.utils.text import slugify
# Create your models here.



class course_category(models.Model):
    class Meta:
        verbose_name_plural = 'Course Category'
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Course_Table(models.Model):
    class Meta:
        verbose_name_plural = 'Course Table'
    Name = models.CharField(max_length=255)
    Class_Qty = models.CharField(max_length=255, default=None, blank=True, null=True)
    Duration = models.CharField(max_length=255, default=None, blank=True, null=True)
    Task = models.CharField(max_length=255, default=None, blank=True, null=True)
    slug = models.SlugField(default="Auto-Generate", editable=False)
    regular_price = models.IntegerField()
    offer_price = models.IntegerField()
    Category = models.ForeignKey(course_category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='course/course_img/', blank=True, null=True)
    Video = models.FileField(upload_to='course/course_video/', blank=True, null=True)
    embed_video = models.CharField(max_length=255, default=None, blank=True, null=True)
    view_option = (
        ('image', 'image'),
        ('video', 'video'),
        ('embed_video', 'embed_video'),
    )
    course_view_select = models.CharField(max_length=255, choices=view_option, default='image', blank=True, null=True)
    Short_Description = RichTextField(blank=True, null=True)
    Description = RichTextField(blank=True, null=True)
    course_file = models.FileField(upload_to="course_file/", blank=True, null=True)
    tags = models.CharField(max_length=255, default="", blank=True, null=True)
    featured = models.BooleanField(default=False)
    Time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.Name


    def save(self, *args, **kwargs):
        # result = readtime.of_text(self.Description)
        result = readtime.of_html(self.Description)
        self.Read_Time = result.text

        # make random order ID
        my_slug = slugify(self.Name)
        uniqe_confirm = Course_Table.objects.filter(slug=my_slug)
        count_num = 0
        while uniqe_confirm:
            count_num = count_num + 1
            my_slug = str(slugify(self.Name))+ "-" + str(count_num)
            if not Course_Table.objects.filter(slug=my_slug):
                break
        if self.slug == "Auto-Generate":
            self.slug = my_slug
        else:
            pass
        super(Course_Table, self).save(*args, **kwargs)


class Course_Checkout_Table(models.Model):
    class Meta:
        verbose_name_plural = 'Course Checkout Table'
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Number = models.CharField(max_length=255)
    Course = models.ForeignKey(Course_Table, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name