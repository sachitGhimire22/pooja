from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField (max_length=50,null=False,default='first')
    lastName = models.CharField(max_length=30,null=False,default="last")
    username =  models.CharField(max_length=30,null=False,default="user")
    password = models.CharField(max_length=40)
    email = models.EmailField(null=True)
    