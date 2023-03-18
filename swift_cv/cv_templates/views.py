from django.shortcuts import render

# Create your views here.
def templates(request):
    return render(request, 'temp1.html')