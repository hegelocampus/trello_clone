from django.shortcuts import render
from django.urls import path, include

from . import views

def index(request):
    return render(request, 'index.html')

urlpatterns = [
    path('', index),
]
