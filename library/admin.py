from django.contrib import admin

# Register your models here.
from .models import studentName, Library, Book
admin.site.register(studentName)
admin.site.register(Library)
admin.site.register(Book)