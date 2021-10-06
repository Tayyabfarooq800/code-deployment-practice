from django.db import models
from django.db.models.deletion import CASCADE


class School(models.Model):
    name = models.CharField(max_length=235)
    principal = models.CharField(max_length = 234)
    location = models.CharField(max_length = 234)


    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length = 234)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School , related_name = "students" , on_delete=CASCADE)


    def __str__(self):
        return self.name

# Create your models here.
