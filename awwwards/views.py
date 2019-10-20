from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from .models import Country
import requests
# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    context={
    'form':form
    }
    return render(request,'register/signup.html',context)
