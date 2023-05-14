from django.db import models

class Student(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    mobile = models.IntegerField()

class Courses(models.Model):
    c_name = models.CharField(max_length=255)
    c_duration = models.IntegerField()
    c_code = models.CharField(max_length=255)
# Create your models here.
