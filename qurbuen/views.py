from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request,'qurbuen/index.html')

def register(request):
    return render(request,'qurbuen/register.html')