from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from .manager import UserManger

class CustomUser(AbstractUser):
    username = None
    phone_number  = models.CharField(max_length=100, unique= True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=800)
    user_profile_image = models.ImageField(upload_to='profile')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']

    objects = UserManger()
