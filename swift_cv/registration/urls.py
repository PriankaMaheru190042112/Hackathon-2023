from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views 


urlpatterns = [
    path('',views.index, name='index'),
    path('registration/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
   
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
