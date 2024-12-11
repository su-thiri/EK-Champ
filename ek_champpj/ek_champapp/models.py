from django.db import models

# Create your models here.

class Round(models.Model):
    round_id = models.CharField(max_length=100)
    championship_name = models.CharField(max_length=100)
    round_name = models.CharField(max_length=100)
    round_date = models.CharField(max_length=100)
    race_status = models.CharField(max_length=100)
    driver_changes = models.CharField(max_length=100)
    track = models.CharField(max_length=100)
    base_weight = models.CharField(max_length=100)
    max_weight = models.CharField(max_length=100)
    race_duration_time = models.CharField(max_length=100)
    pitlane = models.CharField(max_length=100)

class Team_numbers(models.Model):
    team_number_id = models.CharField(max_length=100)
    championship_id = models.CharField(max_length=100)
    team_id = models.CharField(max_length=100)
    team_number = models.CharField(max_length=100)

class Team_in_round(models.Model):
    id = models.IntegerField(primary_key=True)
    championship = models.CharField(max_length=100)
    round = models.CharField(max_length=100)
    team_name = models.CharField(max_length=100)
    team_number = models.CharField(max_length=100)
    start_position = models.CharField(max_length=100)
    finish_position = models.CharField(max_length=100)
    position_points = models.CharField(max_length=100)
    penalty_points = models.CharField(max_length=100)
    total_points = models.CharField(max_length=100)


    