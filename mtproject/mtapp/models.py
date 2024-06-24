from django.db import models

# Create your models here.



class Emp(models.Model):
    name=models.CharField(max_length=30,verbose_name="enter the name")
    age=models.IntegerField(max_length=30,verbose_name="enter the age")
    class Meta:
        db_table="Employee"


class Tech(models.Model):
    first_name=models.CharField(max_length=30)
    photo=models.ImageField(upload_to='images/')

class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField(max_length=30)
    email=models.EmailField(max_length=30)



