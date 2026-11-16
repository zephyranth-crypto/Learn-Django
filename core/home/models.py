from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.AutoField()
    name = models.TextField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null = True)
    address = models.TextField(null = True)