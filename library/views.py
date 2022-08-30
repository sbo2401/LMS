from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import studentName, Book
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def home(request):
  return render(request, 'register.html')

def signup(request):
  
  if request.method == 'POST':
    # username =request.POST.get('username')
    username = request.POST['username']
    fname = request.POST['fname']
    mname = request.POST['mname']
    lname = request.POST['lname']
    email = request.POST['email']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']
    
    myuser = User.objects.create_user(username, email, pass1)
    myuser.first_name=fname
    myuser.mName=mname
    myuser.last_name=lname
    
    myuser.save()
    messages.success(request, "Your account Has been created")
    
    return redirect('signin')
  
  return render(request, 'signup.html')

def signin(request):
  if request.method == 'POST':
    username = request.POST['username']
    pass1 = request.POST['pass1']
     
    user = authenticate(username=username, password=pass1)
    
    if user is not None:
      login(request, user)
      return redirect('user')
    else:
      messages.error(request, "Details not found")
      return redirect('home')
     
    
  return render(request, 'signin.html')

def signout(request):
  return render(request, 'signout.html')

def loginpage(request):
  context ={}
  return render(request, 'login.html', context)

def index(request):
  student = studentName.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'student': student,
  }
  return HttpResponse(template.render(context, request))

def user(request):
  student = studentName.objects.all().values()
  template = loader.get_template('main.html')
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

  