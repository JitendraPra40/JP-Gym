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
    salary=models.IntegerField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
    
class MembershipPlan(models.Model):
    plan=models.CharField(max_length=150)
    price=models.IntegerField()

    def __int__(self):
        return self.id
    
class Gallery(models.Model):
    title=models.CharField(max_length=50)
    img=models.ImageField(upload_to='gallery')
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

class CustAttendance(models.Model):
    phonenumber=models.CharField(max_length=10)
    Workout=models.CharField(max_length=150)
    Date=models.DateTimeField(auto_now_add=True)
    LoginTime=models.CharField(max_length=200)
    LogoutTime=models.CharField(max_length=200)
    TrainedBy=models.CharField(max_length=150)
    Status=models.CharField(max_length=150)

    def __str__(self):
        return f"User: {self.phonenumber}, Date: {self.Date}"
    
class Workout(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

# about us contents
class GymAddress(models.Model):
    title = models.CharField(max_length=255)
    title_des = models.TextField()
    address = models.TextField()
    description = models.TextField()
       
    def __str__(self):
        return self.title


class GymImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class GymContact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f"Contact: {self.email}"


class Facility(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='facilities/')

    def __str__(self):
        return self.title


# services
class Services(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img_service/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.email