from django.contrib import admin
from django.urls import path
from django.shortcuts import render, HttpResponse, Http404

def home(request) :
    return render(request, "home.html", {'title' : 'Modelos disponibles'})

def about(request) :
    return render(request, "about.html", {'title' : ''})
