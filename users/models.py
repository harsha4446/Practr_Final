from django.db import models
from django import forms

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=10)

    def __str__(self):
        return self.name +' - '+ self.username

class student_details(models.Model):
    username=models.ForeignKey(student,on_delete=models.CASCADE)
    creativiy=models.IntegerField(default=0)
    presentation=models.IntegerField(default=0)
    overall=models.IntegerField(default=0)