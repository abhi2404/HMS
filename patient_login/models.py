from django.db import models

# Create your models here.
class patient_login(models.Model):
	name=models.CharField(max_length=20)
	email=models.CharField(max_length=35,unique=True)
	password=models.CharField(max_length=15)
	mobile_no=models.CharField(max_length=10)
	age=models.CharField(max_length=5)
	gender=models.CharField(max_length=10)
	