from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EKPJ(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class EKPJLogin(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class Driver(models.Model):
    id = models.IntegerField(primary_key=True)
    name_en = models.CharField(max_length=255)
    name_th = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    dob = models.DateField()
    qr_code = models.IntegerField()  # Changed from IntegerField to CharField
    age = models.IntegerField()
    profile_picture = models.ImageField(upload_to='driver_images/', null=True, blank=True)

    def __str__(self):
        return self.name_en


class SearchLog(models.Model):
    term = models.CharField(max_length=255)
    searched_at = models.DateTimeField(auto_now_add=True)