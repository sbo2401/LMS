from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import studentName

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

  # output = ""
  # for x in student:
  #   output += x["surname"]
  # return HttpResponse(output)