from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1> Hola mundo desde Django 5.1 </h1>")