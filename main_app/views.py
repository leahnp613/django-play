
from django.http import HttpResponse 
from django.shortcuts import render 

def home(request):
    return HttpResponse('<h1>Hello Kid!</h1>')

def about(request):
    return render(request, 'about.html')
