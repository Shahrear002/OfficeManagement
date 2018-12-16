from django.db import models
from django.forms import ModelForm
from datetime import datetime, timedelta

class employee_info(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class meal_info(models.Model):
    username = models.CharField(max_length=15)
    cost = models.IntegerField(blank=False)
    totalcost = models.IntegerField()
    description = models.CharField(max_length=80)
    dtime = models.DateTimeField(default=datetime.now()+timedelta(days=30))
