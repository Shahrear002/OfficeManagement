from django.db import models
from django.forms import ModelForm

class employee_info(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=20)
    totalcost = models.IntegerField()

    def __str__(self):
        return self.username
