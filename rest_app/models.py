from django.db import models

# Create your models here.
class student_table(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    std=models.CharField(max_length=300)
    def __str__(self):
        return self.name