from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import studentName, Book

def index(request):
  student = studentName.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'student': student,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x=request.POST['fname']
  y=request.POST['mname']
  z=request.POST['lname']
  student=studentName(surname=x, firstname=y, lastname=z)
  student.save()
  return HttpResponseRedirect(reverse('index'))


def book(request):
  book = Book.objects.all().values()
  template = loader.get_template('books.html')
  context = {
    'book': book,
  }
  return HttpResponse(template.render(context, request))

def addbook(request):
  template = loader.get_template('addbook.html')
  return HttpResponse(template.render({}, request))

def todb(request):
  a=request.POST['title']
  b=request.POST['author']
  c=request.POST['publisher']
  d=request.POST['year']
  e=request.POST['price']
  book=Book(Title=a, Author=b, Publisher=c, Year=d, Price=e)
  book.save()
  return HttpResponseRedirect(reverse('book'))

  # output = ""
  # for x in student:
  #   output += x["surname"]
  # return HttpResponse(output)