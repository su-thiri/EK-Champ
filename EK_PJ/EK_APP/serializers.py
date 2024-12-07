from rest_framework import serializers
from .models import Driver

class EKPJSerializer(serializers.Serializer):
    username=serializers.CharField(label="Enter Your Username")
    password=serializers.CharField(label="Enter Your Password")

class EKPJSerializerLogin(serializers.Serializer):
    username=serializers.CharField(label="Enter Your Username")
    password=serializers.CharField(label="Enter Your Password")

class DriverSerializer(serializers.ModelSerializer):
    profile_picture_url = serializers.SerializerMethodField()

    class Meta:
        model = Driver
        fields = ['id', 'name_en', 'name_th', 'nickname', 'dob', 'qr_code', 'age', 'profile_picture', 'profile_picture_url']

    def get_profile_picture_url(self, obj):
        if obj.profile_picture:
            return obj.profile_picture.url
        return None
