from django.db import models

# Create your models here.
class Conatct(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.email

class enrollment(models.Model):
    FullName = models.CharField(max_length=50)
    Email = models.EmailField()
    Gender = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=10)
    DOB = models.models.DateField(auto_now=False, auto_now_add=False)
    SelectMembershipPlan = models.CharField(max_length=50)
    SelectTrainer = models.CharField(max_length=50)
    reference= models.CharField(max_length=50)  
    Address = models.TextField()
    timeStamp= models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.FullName

class Trainer(models.Model):
    name = models.CharField(max_length=50)
    gender=models.charField(max_length=25)
    phone=models.charField(max_length=10)
    salary=models.IntegerField(max_length=25)
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
    
class MemebershipPlan(models.Model):
    plan=models.CharField(max_length=150)
    price=models.IntegerField(max_length=55)

    def __int__(self):
        return self.id