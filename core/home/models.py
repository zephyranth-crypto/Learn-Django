from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.AutoField()
    name = models.TextField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True)
    address = models.TextField(null=True)

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    car_speed = models.IntegerField(default=50) 

    def __str__(self) -> str:
        return self.car_name
print("check")