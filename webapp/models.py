from statistics import mode
from django.db import models

class employees(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstname
