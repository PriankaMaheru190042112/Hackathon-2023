from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView,TemplateView
from cv_templates.models import CV_template,CV_type
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import *

# Create your views here.
def home(request):
    cvs= CV_type.objects.all()
    cvlists= CV.objects.all()
    context={
        'cvs': cvs,
        'cvlists': cvlists
    }
    return render(request, 'home.html', context)
    

def create_cv(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        linked_in= request.POST.get('linked_in')
        github= request.POST.get('github')
        image= request.FILES.get('image')

        inst_name = request.POST.getlist('inst_name')
        result= request.POST.getlist('result')
        skill= request.POST.getlist('skill_name')
        ach= request.POST.getlist('ach_name')

       
        
        u= CV.objects.create(name=name, email=email, phone_number=phone, linked_in=linked_in , github=github, image=image, )
            
        print(inst_name)

            
        for i,x in zip(inst_name,result):
            
                inst  = Institution.objects.create(cv_id=u, inst_name=i,result=x)
                inst.save() 

        for j in skill:
            
                skill  = Skill.objects.create(cv_id=u, skill_name=j,skill_level=0)
                skill.save() 
        for k in ach:
            
                ach  = Achievement.objects.create(cv_id=u, ach_name=k)
                ach.save() 
        
            
        u.save()
        return redirect('/preview')
        
    
    return render(request, 'create_cv.html')
 
def cvPreview(request):
    cvs= CV.objects.all()
    context={
          'cvs':cvs
    }

    return render(request, 'preview_cv.html',context)

def update(request):
    return render(request, 'update_cv.html')