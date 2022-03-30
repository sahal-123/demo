from django.db import models

# Create your models here.
class student(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    username=models.CharField(max_length=40)
    password=models.IntegerField()

class login1(models.Model):
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=40)

