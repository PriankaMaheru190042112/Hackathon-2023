from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def SignupPage(request):
    return render(request, 'signup.html')

def LoginPage(request):
    return render(request, 'login.html')