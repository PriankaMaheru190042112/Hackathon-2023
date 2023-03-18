from django.db import models

# Create your models here.
class CV_template(models.Model):
    temp_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,null= False)
    type = models.CharField( max_length=200,null= False)
   
    def __str__(self):
        return str(self.name)