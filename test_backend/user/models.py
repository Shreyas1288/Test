from django.db import models

# Create your models here.
class Dataset(models.Model):
    yop = models.IntegerField()
    sp = models.IntegerField()
    dist = models.IntegerField()
    owners = models.IntegerField()
    fuel = models.CharField(max_length = 20, default = 'petrol')
    owner_type = models.CharField(max_length = 20, default ='individual')
    transmission = models.CharField(max_length = 20, default = 'manual')

