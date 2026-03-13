from django.db import models


# Create your models here.
class Challenge(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

class Rtag(models.Model):
    owner_id = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    challenge_id = models.CharField(max_length=25)
    longitude = models.DecimalField(
        max_digits=20,
        max_length=40,
        decimal_places=20
    )
    latitude = models.DecimalField(
        max_digits=20,
        max_length=40,
        decimal_places=20
    )
    elevation = models.DecimalField(
        max_digits=20,
        max_length=40,
        decimal_places=20
    )

class Scoreboard(models.Model):
    scoreboard_version = models.CharField(max_length=30)

class User(models.Model):
    user_handle = models.CharField(max_length=30)