# models.py
from django.db import models
from django.utils import timezone

class Team(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    address = models.CharField(max_length=50, default="Gasanze")
    school_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    parent_tel = models.CharField(max_length=15)

    class Meta:
        ordering = ['first_name','last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Attend(models.Model):
    member = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member} - {self.date} - {'Present' if self.present else 'Absent'}"
    



    
class HandballMember(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    address = models.CharField(max_length=50, default="Gasanze")
    school_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    parent_tel = models.CharField(max_length=15)

    class Meta:
        ordering = ['first_name','last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"    
    

class VolleballMember(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    address = models.CharField(max_length=50, default="Gasanze")
    school_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    parent_tel = models.CharField(max_length=15)

    class Meta:
        ordering = ['first_name','last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  
    
class BasketBall(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    address = models.CharField(max_length=50, default="Gasanze")
    school_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    parent_tel = models.CharField(max_length=15)

    class Meta:
        ordering = ['first_name','last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  
    
class MinFoot(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    address = models.CharField(max_length=50, default="Gasanze")
    school_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    parent_tel = models.CharField(max_length=15)

    class Meta:
        ordering = ['first_name','last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  
    
class Karate(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    address = models.CharField(max_length=50, default="Gasanze")
    school_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    parent_tel = models.CharField(max_length=15)

    class Meta:
        ordering = ['first_name','last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  
class Tradition(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    address = models.CharField(max_length=50, default="Gasanze")
    school_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    parent_tel = models.CharField(max_length=15)

    class Meta:
        ordering = ['first_name','last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"