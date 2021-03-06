"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from qurbuen.views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('index/', index, name='index'),
    path('hukum/', hukum, name='hukum'),
    path('tentang/', tentang, name='tentang'),
    path('admin/', admin.site.urls),
    path('beliqurban1/', beliqurban1, name='Beli Qurban'),
    path('beliqurban2/', beliqurban2, name='Beli Qurban'),
    path('beliqurban3/', beliqurban3, name='Beli Qurban'),
]
