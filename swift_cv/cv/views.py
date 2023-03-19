from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView
from cv_templates.models import CV_template,CV_type
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def home(request):
    cvs= CV_type.objects.all()

    context={
        'cvs': cvs
    }
    return render(request, 'home.html', context)
    

def create_cv(request):
    return render(request, 'create_cv.html')


class cvPreview(TemplateView):
    template_name= 'preview_cv.html'

def update(request):
    return render(request, 'update_cv.html')

def navigation(request):
    return render(request, 'navigation.html')