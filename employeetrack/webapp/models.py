from django.db import models
from django.forms import ModelForm
from django.utils import timezone

class employee_info(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
