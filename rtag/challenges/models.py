from django.db import models


# Create your models here.
class Challenge(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
