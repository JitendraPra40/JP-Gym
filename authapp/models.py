from django.db import models

# Create your models here.
class Conatct(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.email