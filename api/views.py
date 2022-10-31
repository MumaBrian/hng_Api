from django.shortcuts import render
from rest_framework import generics
from .serializers import ApiSerializer,RegisterSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.response import Response

from .models import Api
# Create your views here.
class ListApi(generics.ListAPIView):
    queryset=Api.objects.all()
    serializer_class=ApiSerializer


  
 

# #Class based view to register user
# class RegisterUserAPIView(generics.CreateAPIView):
#   permission_classes = (AllowAny,)
#   queryset=Api.objects.all()

#   serializer_class = RegisterSerializer