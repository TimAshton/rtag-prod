from django.db import models


# Create your models here.
class Scoreboard(models.Model):
    scoreboard_version = models.CharField(max_length=30)
