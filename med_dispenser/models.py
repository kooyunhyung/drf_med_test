from django.db import models

# Create your models here.
class med_dispenser(models.Model):
    title = models.CharField(max_length=200)
    bloodSugar = models.IntegerField()
    bloodPressure_high = models.IntegerField()
    bloodPressure_low = models.IntegerField()
    liverShame = models.IntegerField()