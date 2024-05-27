 
from django.db import models

class CSVData(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    subscription_price = models.FloatField()

    def __str__(self):
        return self.name
