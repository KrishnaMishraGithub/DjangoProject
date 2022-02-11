#from os import name
from django.contrib import admin
from django.urls import path
from HomeApp import views


urlpatterns = [
    path("index",views.index, name='home'),
    path("about",views.about, name='about us'),
    path("contact",views.contact,name='conatct'),
    path("services",views.services,name='services')
]