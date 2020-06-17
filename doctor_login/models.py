from django.db import models

# Create your models here.
class doctor_login(models.Model):
	name=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	password=models.CharField(max_length=10)
	doctor_degree=models.CharField(max_length=50)
	mobile_no=models.CharField(max_length=12,null=True,blank=True)
	field=models.CharField(max_length=20,null=True)
	status=models.CharField(max_length=10,default="pending")

class doctor_degree(models.Model):
	degree=models.CharField(max_length=50)

class specialization(models.Model):
	field=models.CharField(max_length=20)
	link=models.ForeignKey('doctor_degree',models.DO_NOTHING)
	