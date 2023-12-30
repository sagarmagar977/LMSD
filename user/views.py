
from django.shortcuts import render
from .models import User
from .serializers import *

from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
    
from django.contrib.auth.hashers import make_password

from rest_framework import viewsets,mixins
from core.permission import CustomModelPermission

from rest_framework.views import APIView



####################################################
################## [ LOGIN] ########################
####################################################
@api_view(['POST'])
@permission_classes([AllowAny])

def Login(request):
    email=request.data.get('email')
    password=request.data.get('password')
    user=authenticate(username=email,password=password)
    if user is None:
        return Response("Invalid email or password ! ")
    else :
        token,_=Token.objects.get_or_create(user=user)
        return Response({'token':token.key})
    


####################################################
############## [ REGISTER ] ########################
####################################################
    
from django.contrib.auth.hashers import make_password
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    password=request.data.get('password')
    request.data['password']=make_password(password)
    serializers=UserSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response("Congratulaion ! User is created ! ")
    else :
        return Response(serializers.errors)
    
##########################################
############## [ GROUP VIEW ] ############
##########################################


class GroupView(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset=Group.objects.all()
    serializer_class=groupserializers
    permission_classes=[CustomModelPermission]

#############################################
############## [ USER VIEW ] ################
#############################################

class userview(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset=User.objects.all()
    serializer_class=CustomUserInfoSerilaizers
    permission_classes=[CustomModelPermission]


    

 
class UsersByGroupAPIView(APIView):
    def get(self, request, group_name):
        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            return Response({"error": f"Group with name '{group_name}' does not exist."})

        users = group.user_set.all()
        serializer = CustomUserInfoSerilaizers(users, many=True)
        return Response(serializer.data)

