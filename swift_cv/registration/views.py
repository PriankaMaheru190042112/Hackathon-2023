from multiprocessing import AuthenticationError
from pickle import NONE
from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render
from .models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



# Create your views here.
@csrf_exempt
def index(request):
    return render(request, 'index.html')
def SignupPage(request):
    if request.method=='POST':
        first_name = request.POST.get('Firstname')
        last_name = request.POST.get('Lastname')
        email = request.POST.get('Email')
        password1 = request.POST.get('Password')
        password2 = request.POST.get('Retype')

        my_user=User.objects.create_user(username= first_name,first_name=first_name,last_name=last_name,email=email,password=password1)
        my_user.save()

        return redirect('login')
        
       

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username = request.POST['username']
        psw = request.POST['psw']
        user = authenticate(request, username=username, password=psw)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse ("Username or password is incorrect!!!")

    return render (request,'login.html')