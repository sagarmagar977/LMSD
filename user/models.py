from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username=models.CharField(default='user',null=True,max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=100)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

