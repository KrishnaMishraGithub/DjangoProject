from django.db import models



# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=120,null= True)
    email=models.CharField(max_length=120,null= True)
    phone=models.CharField(max_length=12,null= True)
    desc=models.TextField()
    date=models.DateTimeField()

def __str__(self):
    return self.name
  