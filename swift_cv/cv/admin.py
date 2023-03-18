from django.contrib import admin
from .models import CV, Skill, Institution, Achievement

admin.site.register(CV)
admin.site.register(Skill)
admin.site.register(Institution)
admin.site.register(Achievement)

# Register your models here.
