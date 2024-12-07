from rest_framework import serializers

class EKPJSerializer(serializers.Serializer):
    username=serializers.CharField(label="Enter Your Username")
    password=serializers.CharField(label="Enter Your Password")

class EKPJSerializerLogin(serializers.Serializer):
    username=serializers.CharField(label="Enter Your Username")
    password=serializers.CharField(label="Enter Your Password")