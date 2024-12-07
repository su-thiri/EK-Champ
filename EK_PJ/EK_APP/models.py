from django.db import models

class EKPJ(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "EKPJ User"
        verbose_name_plural = "EKPJ Users"


class EKPJLogin(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "EKPJ Login"
        verbose_name_plural = "EKPJ Logins"


class Driver(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)  # Allow users to input their own ID, ensuring uniqueness
    name_en = models.CharField(max_length=255)
    name_th = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    dob = models.DateField()
    qr_code = models.IntegerField()
    age = models.IntegerField()
    profile_picture = models.ImageField(upload_to='driver_images/', null=True, blank=True)

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"
