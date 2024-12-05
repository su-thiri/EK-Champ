from django.db import models

# Create your models here.
class EKPJ(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class EKPJLogin(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)