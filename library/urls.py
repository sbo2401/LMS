from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('', views.index, name='index'),
    path('user/', views.user, name='user'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('book/', views.book, name='book'),
    path('book/addbook/', views.addbook, name='addbook'),
    path('book/addbook/todb/', views.todb, name='todb')
] 