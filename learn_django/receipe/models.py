from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receipe(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    # models.CASCADE = delete all the receipes realted to the user
    # models.SET_NULL = sets value null if user is removed 
    # models.SET_DEFAULT = to set default value  
    receipe_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=800)
    image = models.FileField(upload_to='receipe/')

    def __str__(self):
        return self.receipe_name
