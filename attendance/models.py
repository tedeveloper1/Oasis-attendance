# models.py
from django.db import models
from django.utils import timezone

class Team(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.DateField(default=timezone.now)
    school_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    address = models.CharField(max_length=50, default="Gasanze")
    parent_tel = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Attend(models.Model):
    member = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member} - {self.date} - {'Present' if self.present else 'Absent'}"
