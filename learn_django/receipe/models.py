from django.db import models

# Create your models here.

class Receipe(models.Model):
    receipe_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=800)
    image = models.FileField(upload_to='receipe/')

    def __str__(self):
        return self.receipe_name