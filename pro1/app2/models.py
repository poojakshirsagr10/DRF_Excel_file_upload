from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

class Student1(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    roll = models.IntegerField()
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=50)