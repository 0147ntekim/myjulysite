from django.contrib import admin
from django.urls import path,include 
from . import views


urlpatterns = [
    path('', views.user, name='user'),
    path('index/', views.index, name='index'),
    path('company/', views.company, name='company'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('video/', views.video, name='video'),
    path('table/', views.table, name='table'),
    path('update/<int:id>/', views.update, name='update'),
    path('clear/<int:id>/', views.clear, name='clear')
]
