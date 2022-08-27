from django.db import models

# Create your models here.
class studentName(models.Model):
    surname = models.CharField(max_length=255, default="")
    firstname = models.CharField(max_length=255, default="")
    lastname = models.CharField(max_length=255, default="")

class Library(models.Model):
    catalog = models.CharField(max_length=255, default="")
    collections = models.CharField(max_length=75, default="")

class Book(models.Model):
    Title = models.CharField(max_length=255, default="")
    Author = models.CharField(max_length=255, default="")
    Publisher = models.CharField(max_length=255, default="")
    Year = models.CharField(max_length=4, default="")
    Price = models.DecimalField(max_digits=15, decimal_places=2)