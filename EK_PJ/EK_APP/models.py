from django.db import models

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
    qr_code = models.IntegerField()  # You might want to consider a `CharField` for QR codes if needed
    age = models.IntegerField()
    profile_picture = models.ImageField(upload_to='driver_images/', null=True, blank=True)

    def __str__(self):
        return self.name_en  # String representation of the object