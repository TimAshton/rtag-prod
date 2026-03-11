from django.db import models

# Create your models here.
class Challenge(models.Model):
    challenge_title = models.CharField(max_length=60)
    challenge_description = models.TextField()
    challenge_created_date = models.DateTimeField(auto_now=True)