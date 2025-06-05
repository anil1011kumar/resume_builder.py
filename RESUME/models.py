from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    institute = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    marks = models.IntegerField()
    project = models.CharField(max_length=50)
    skills = models.CharField(max_length=100)
    about = models.CharField(max_length=250)


 