from django.core.exceptions import FieldDoesNotExist
from django.db import models


# Create your models here.


class Student(models.Model):
    fullname = models.CharField(max_length=50, blank=True, default='')
    score = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname
