from dataclasses import fields
from .models import Api
from rest_framework import serializers

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Api
        fields=['slackUsername','backend','age','bio']


class RegisterSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    # required=True )
    # password = serializers.CharField(
    # write_only=True, required=True)
    # password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
       model = Api
       fields = ('slackUsername','backend','age','bio')
       
      
 
  