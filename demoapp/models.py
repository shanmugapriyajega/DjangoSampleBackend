from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
# User=get_user_model()
# Create your models here.
class demotable(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=250)

    def __str__(self):
        return self.name
class dresscategorytable(models.Model):
    categoryname=models.CharField(max_length=300)
    def __str__(self):
        return self.categoryname
class dresstable(models.Model):
    id=models.AutoField(primary_key=True)
    dressname=models.CharField(max_length=300)
    dressprice=models.CharField(max_length=200)
    dressimg=models.URLField()
    dresscategory=models.ForeignKey(dresscategorytable,on_delete=models.CASCADE)
    def __str__(self):
        return self.dressname          

class otherdetails(AbstractUser):
    user_address=models.CharField(max_length=300)
    user_phnnum=models.IntegerField(null=True)
    def __str__(self):
        return self.username