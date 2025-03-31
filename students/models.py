from django.db import models

# Create your models here.

class Student(models.Model):
    std_id = models.IntegerField()
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)

    def __str__(self):
        return  self.name
