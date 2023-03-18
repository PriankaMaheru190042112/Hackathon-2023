from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views 



urlpatterns = [
    path('template', views.templates, name='templates'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
