from rest_framework import serializers
from .models import Driver

class EKPJSerializer(serializers.Serializer):
    username = serializers.CharField(label="Enter Your Username")
    password = serializers.CharField(label="Enter Your Password")

class EKPJSerializerLogin(serializers.Serializer):
    username = serializers.CharField(label="Enter Your Username")
    password = serializers.CharField(label="Enter Your Password")

class DriverSerializer(serializers.ModelSerializer):
    profile_picture_url = serializers.SerializerMethodField()

    class Meta:
        model = Driver
        fields = ['id', 'name_en', 'name_th', 'nickname', 'dob', 'qr_code', 'age', 'profile_picture', 'profile_picture_url']

    def get_profile_picture_url(self, obj):
        if obj.profile_picture:
            return obj.profile_picture.url
        return None

    # Optional: Custom validation for the `id` field to ensure the `id` is unique
    def validate_id(self, value):
        if Driver.objects.filter(id=value).exists():
            raise serializers.ValidationError("ID already exists. Please choose a unique ID.")
        return value

    # Optional: Validation for `age` to ensure it is a positive number
    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError("Age must be a positive integer.")
        return value

    # Optional: You could add custom validation for `profile_picture` if required
    def validate_profile_picture(self, value):
        if value and value.size > 5 * 1024 * 1024:  # 5MB size limit
            raise serializers.ValidationError("Profile picture file size exceeds the 5MB limit.")
        return value
