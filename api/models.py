from django.db import models

# Create your models here.

class Sensor(models.Model):
    value = models.FloatField()
    created_at = models.DateField(null= True)