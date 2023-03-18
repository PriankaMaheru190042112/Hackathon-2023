from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView

# Create your views here.
class home(TemplateView):
    template_name = 'home.html'

def create_cv(request):
    return render(request, 'create_cv.html')


class cvPreview(TemplateView):
    template_name= 'preview_cv.html'

def update(request):
    return render(request, 'update_cv.html')