from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request,'qurbuen/index.html')

def register(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registrasi Berhasil")
            return redirect('login')
        else:
             messages.error(request, "Registrasi Gagal")
             return redirect('register')
    else:
        form =  UserCreationForm()
        context = {
            'form':form,
        }
    return render(request,'register.html', context)

<<<<<<< Updated upstream
def hukum(request):
    return render(request, 'qurbuen/hukum.html')

def tentang(request):
    return render(request, 'qurbuen/tentang.html')
=======
def beliqurban1(request):
    return render(request,'qurbuen/beliqurban1.html')

def beliqurban2(request):
    return render(request,'qurbuen/beliqurban2.html')

def beliqurban3(request):
    return render(request,'qurbuen/beliqurban3.html')
>>>>>>> Stashed changes
