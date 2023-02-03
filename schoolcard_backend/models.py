from django.db import models


# Create your models here.


class Student(models.Model):
    objects = models.Manager()
    student_id = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    student_balance = models.FloatField()
