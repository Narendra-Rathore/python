from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20, default="")
    subject = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    message = models.CharField(max_length=255, default="")
    date = models.DateField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    title = models.CharField(max_length=50)
    percent = models.CharField(max_length=3)
    date = models.DateField()

    def __str__(self):
        return self.title

class Reference(models.Model):
    name = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.name

        