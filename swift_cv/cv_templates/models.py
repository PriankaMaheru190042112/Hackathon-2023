from django.db import models

# Create your models here.

class CV_type(models.Model):
    type_id=  models.AutoField(primary_key=True)
    type=models.CharField(max_length=200,null= False) 

    def __str__(self):
        return str(self.type)

    @property
    def get_products(self):
         return CV_template.objects.filter(type=self.type_id)

class CV_template(models.Model):
    temp_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,null= False)
    type = models.ForeignKey(CV_type, on_delete=models.CASCADE)
   
    def __str__(self):
        return str(self.name)
    