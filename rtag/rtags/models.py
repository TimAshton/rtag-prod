from django.db import models

# Create your models here.
class Rtag(models.Model):
    rtag_owner_id = models.CharField(max_length=50)
    rtag_title = models.CharField(max_length=150)
    rtag_longitude = models.DecimalField(max_digits=20, max_length=40, decimal_places=20)
    rtag_latitude = models.DecimalField(max_digits=20, max_length=40, decimal_places=20)
    rtag_elevation = models.DecimalField(max_digits=20, max_length=40, decimal_places=20)