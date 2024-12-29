from django.db import models

# Create your models here.

class Student(models.Model):
    # without primary_key=True parmeter for column 'id' it gives error 
    # ValueError: Model basics.Student can't have more than one auto-generated field.
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=40)
    age= models.IntegerField(null=True, blank=True)
    rollno= models.IntegerField(null=True, blank=True)
    email= models.EmailField()
    address= models.CharField(max_length=600)
    image= models.ImageField()
    file= models.FileField()
    

class Car(models.Model):
    car_name= models.CharField(max_length=100, blank=False)
    speed = models.IntegerField(null=True)

    def __str__(self):
        return self.car_name

