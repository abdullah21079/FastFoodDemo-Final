from django.db import models

# Create your models here.
class Payment(models.Model):
    name=models.CharField(max_length=50)
    epin=models.IntegerField(default=True)

    