from django.contrib import admin
from django.shortcuts import render, HttpResponse, Http404
from django.urls import path

def home(request) :
    return render(request, "home.html")
