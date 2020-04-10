from django.contrib import admin
from django.urls import path
from django.shortcuts import render, HttpResponse, Http404

def home(request) :
    return render(request, "home.html", {'title' : 'Modelos disponibles', 'home' : 'active'})

def about(request) :
    return render(request, "about.html", {'title' : '', 'about' : 'active'})

def contact(request) :
    return render(request, "contact.html", {'title' : '', 'contact' : 'active'})
