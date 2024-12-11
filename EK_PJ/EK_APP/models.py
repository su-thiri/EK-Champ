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
    qr_code = models.IntegerField()
    age = models.IntegerField()
    profile_picture = models.ImageField(upload_to='driver_images/', null=True, blank=True)

    def __str__(self):
#<<<<<<< Updated upstream
        return self.name_en  # String representation of the object


class SearchLog(models.Model):
    term = models.CharField(max_length=255)
    searched_at = models.DateTimeField(auto_now_add=True)

class Round(models.Model):
    round_id = models.IntegerField(primary_key=True)
    round_name = models.CharField(max_length=255)
    round_date = models.DateField()
    round_base_weight = models.IntegerField()
    round_max_weight = models.IntegerField()
    round_changes = models.IntegerField()
    round_pit_lane = models.IntegerField()
    champion_id = models.IntegerField()
    track_id = models.IntegerField()
    race_status = models.IntegerField()
    durition_min = models.IntegerField()

    def __str__(self):
        return self.round_name

