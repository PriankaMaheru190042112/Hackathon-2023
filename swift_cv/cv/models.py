from django.db import models
from django.urls import reverse
from registration.models import User

# Create your models here.
class CV(models.Model):
    cv_id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone_number= models.IntegerField(max_length=200)
    image=models.ImageField(upload_to='media/',max_length=200)
    linked_in=models.CharField(max_length=200)
    github=models.CharField(max_length=200)


    def __str__(self):
        return str(self.cv_id)
    
    def get_absolute_url1(self):
        return reverse('cv:home', kwargs={'pk': self.pk})

class Institution(models.Model):
    cv_id= models.ForeignKey(CV, on_delete=models.CASCADE)
    inst_name= models.CharField(max_length=200)
    result= models.FloatField(max_length=200)

    def __str__(self):
        return str(self.cv_id)


class Skill(models.Model):
    cv_id= models.ForeignKey(CV, on_delete=models.CASCADE)
    skill_name=models.CharField(max_length=200)
    skill_level= models.IntegerField(max_length=200)

    def __str__(self):
        return str(self.cv_id)

class Experience(models.Model):
    cv_id= models.ForeignKey(CV, on_delete=models.CASCADE)
    company= models.CharField(max_length=200)
    position= models.CharField(max_length=200)
    years= models.IntegerField(max_length=200)

    def __str__(self):
        return str(self.cv_id)
    

class Achievement(models.Model):
    cv_id= models.ForeignKey(CV, on_delete=models.CASCADE)
    ach_name= models.CharField(max_length=200)


    def __str__(self):
        return str(self.cv_id)