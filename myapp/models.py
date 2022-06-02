from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.
class Details(models.Model):
    name= models.CharField(max_length=20)
    address = models.CharField(max_length=20)

class nation(models.Model):
    name= models.CharField(max_length=20)
    