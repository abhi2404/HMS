from django.db import models

# Create your models here.
class doctor_login(models.Model):
	name=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	password=models.CharField(max_length=10)
	doctor_degree=models.CharField(max_length=10)
	mobile_no=models.CharField(max_length=12,null=True,blank=True)
	status=models.CharField(max_length=10,default="pending")

