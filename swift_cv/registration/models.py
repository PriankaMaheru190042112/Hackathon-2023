from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    isUser = models.BooleanField(default=False, null=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)
    profile_picture = models.ImageField(max_length=200, null=True)
    isAdmin = models.BooleanField(default=True, null=False)
 