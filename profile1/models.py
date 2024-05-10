# profile1/models.py
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=16)
    email = models.EmailField()
    address = models.TextField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name
