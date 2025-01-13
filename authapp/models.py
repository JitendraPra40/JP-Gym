from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.email

class Enrollment(models.Model):
    FullName = models.CharField(max_length=50)
    Email = models.EmailField()
    Gender = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=10)
    DOB = models.DateField(auto_now=False, auto_now_add=False)
    SelectMembershipPlan = models.CharField(max_length=50)
    SelectTrainer = models.CharField(max_length=50)
    reference= models.CharField(max_length=50)  
    Address = models.TextField()
    paymentStatus = models.CharField(max_length=50, blank=True, null=True)  
    Price = models.IntegerField(blank=True, null=True)
    DueDate= models.DateField(blank=True, null=True)
    timeStamp= models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.FullName

class Trainer(models.Model):
    name = models.CharField(max_length=50)
    gender=models.CharField(max_length=25)
    phone=models.CharField(max_length=10)
    salary=models.IntegerField(max_length=25)
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
    
class MembershipPlan(models.Model):
    plan=models.CharField(max_length=150)
    price=models.IntegerField(max_length=55)

    def __int__(self):
        return self.id
    
class Gallery(models.Model):
    title=models.CharField(max_length=50)
    img=models.ImageField(upload_to='gallery')
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
