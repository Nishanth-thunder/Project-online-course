from django.db import models

class Course(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    instructor=models.CharField(max_length=300)
    courseimg=models.ImageField(upload_to='images/')


