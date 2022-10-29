from dataclasses import fields
from .models import Api
from rest_framework import serializers

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Api
        fields=['slackUsername','backend','age','bio']