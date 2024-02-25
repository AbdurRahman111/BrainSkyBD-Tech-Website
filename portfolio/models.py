from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
 
#PORTFOLIO CODES
class Portfolio_Category(models.Model):
    class Meta:
        verbose_name_plural = 'Portfolio Category'
    name = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    class Meta:
        verbose_name_plural = 'Portfolio'
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Portfolio_Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/')
    links = models.URLField(max_length=200)

    def __str__(self):
        return self.title


class Pro_Customers(models.Model):
    class Meta:
        verbose_name_plural = 'Pro Customers'
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Pro_Customers/')
    links = models.URLField(max_length=200)

    def __str__(self):
        return self.title


class Portfolio_Details(models.Model):
    class Meta:
        verbose_name_plural = 'Portfolio Details'
    portfolio = models.OneToOneField(Portfolio, on_delete = models.CASCADE)
    description = models.TextField(blank=False)
    date = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    project_image1 = models.ImageField(upload_to='portfolio_details/')
    project_image2 = models.ImageField(upload_to='portfolio_details/')
    project_image3 = models.ImageField(upload_to='portfolio_details/')
    analysis = models.TextField(blank=False)


class contact_form(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Form'
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()
    def __str__(self):
        return self.name


class Newsletter_Table(models.Model):
    class Meta:
        verbose_name_plural = 'Newsletter Table'
    email = models.CharField(max_length=255)
    def __str__(self):
        return self.email