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
class Hand_Attend(models.Model):
    member = models.ForeignKey(HandballMember, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member} - {self.date} - {'present' if self.present else 'Absent'}"

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
class Vally_Attend(models.Model):
    member = models.ForeignKey(VolleballMember, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member} - {self.date} - {'present' if self.present else 'Absent'}"
    
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
    
class Bask_Attend(models.Model):
    member = models.ForeignKey(BasketBall, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    present= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member} - {self.date} - {'present' if self.present else 'Absent'}"

    
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

class Min_Attend(models.Model):
    member = models.ForeignKey(MinFoot, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    present= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member} - {self.date} - {'present' if self.present else 'Absent'}" 
    
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

class Karate_Attend(models.Model):
    member = models.ForeignKey(Karate, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    present= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member} - {self.date} - {'present' if self.present else 'Absent'}" 
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
    
class Tradition_Attend(models.Model):
    member = models.ForeignKey(Tradition, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    present= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member} - {self.date} - {'present' if self.present else 'Absent'}"