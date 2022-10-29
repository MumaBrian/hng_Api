from django.shortcuts import render
from rest_framework import generics
from .serializers import ApiSerializer
from .models import Api
# Create your views here.
class ListApi(generics.ListAPIView):
    queryset=Api.objects.all()
    serializer_class=ApiSerializer