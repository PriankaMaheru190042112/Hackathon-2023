from django.contrib import admin
from .models import CV, Skill,Achievement,Institution

# Register your models here.
admin.site.register(CV)
admin.site.register(Skill)
admin.site.register(Achievement)
admin.site.register(Institution)
