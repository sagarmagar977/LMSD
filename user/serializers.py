from .models import *
from django.contrib.auth.models import Group
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','password','groups']

class groupserializers(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields=['id','name']

class CustomUserInfoSerilaizers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','groups']
