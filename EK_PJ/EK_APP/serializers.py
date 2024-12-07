from rest_framework import serializers
from .models import Driver

class EKPJSerializer(serializers.Serializer):
    username=serializers.CharField(label="Enter Your Username")
    password=serializers.CharField(label="Enter Your Password")

class EKPJSerializerLogin(serializers.Serializer):
    username=serializers.CharField(label="Enter Your Username")
    password=serializers.CharField(label="Enter Your Password")

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'