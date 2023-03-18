from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views 
from .views import home, cvPreview


urlpatterns = [
    path('home',home.as_view(), name='home'),
    path('create',views.create_cv, name='create'),
    path('preview',cvPreview.as_view(),name='preview'),
    path('update',views.update, name='update' )
]
