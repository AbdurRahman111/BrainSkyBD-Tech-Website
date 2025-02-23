from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
import readtime
from django.utils.text import slugify
# Create your models here.



class digital_product_category(models.Model):
    class Meta:
        verbose_name_plural = 'Digital Product Category'
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Digital_Product_Table(models.Model):
    class Meta:
        verbose_name_plural = 'Digital Product Table'
    Name = models.CharField(max_length=255)
    slug = models.SlugField(default="Auto-Generate", editable=False)
    regular_price = models.IntegerField()
    offer_price = models.IntegerField()
    Category = models.ForeignKey(digital_product_category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='digital_product/digital_product_img/', blank=True, null=True)
    Video = models.FileField(upload_to='digital_product/digital_product_video/', blank=True, null=True)
    embed_video = models.CharField(max_length=255, default=None, blank=True, null=True)
    
    Short_Description = RichTextField(blank=True, null=True)
    Description = RichTextField(blank=True, null=True)

    view_option = (
        ('image', 'image'),
        ('video', 'video'),
        ('embed_video', 'embed_video'),
    )
    course_view_select = models.CharField(max_length=255, choices=view_option, default='image', blank=True, null=True)
    
    payment_url = models.URLField(max_length=255, default=None, blank=True, null=True)
    Product_file = models.FileField(upload_to="Product_file/", blank=True, null=True)
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
        uniqe_confirm = Digital_Product_Table.objects.filter(slug=my_slug)
        count_num = 0
        while uniqe_confirm:
            count_num = count_num + 1
            my_slug = str(slugify(self.Name))+ "-" + str(count_num)
            if not Digital_Product_Table.objects.filter(slug=my_slug):
                break
        if self.slug == "Auto-Generate":
            self.slug = my_slug
        else:
            pass
        super(Digital_Product_Table, self).save(*args, **kwargs)


class Digital_Product_Purchase_Table(models.Model):
    class Meta:
        verbose_name_plural = 'Digital Product Purchase Table'
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Number = models.CharField(max_length=255)
    Digital_Product = models.ForeignKey(Digital_Product_Table, on_delete=models.CASCADE)

    status_option = (
        ("Pending", "Pending"),
        ("Complete", "Complete"),
        ("Cancelled", "Cancelled")
    )
    status = models.CharField(max_length=255, choices=status_option, default="Pending")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name