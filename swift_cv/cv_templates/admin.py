from django.contrib import admin

# Register your models here.
from .models import CV_template,CV_type
admin.site.register(CV_template)
admin.site.register(CV_type)