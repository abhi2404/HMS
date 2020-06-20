from django.db import models
from patient_login.models import patient_login

# Create your models here.
class patient_appointment(models.Model):
	booking_date=models.DateTimeField(auto_now_add=True,blank=True)
	date_of_appointment=models.CharField(max_length=15)
	time_of_appointment=models.CharField(max_length=15)
	problem=models.CharField(max_length=200)
	status=models.CharField(max_length=20,default="pending")
	fees=models.CharField(max_length=10,null=True)
	doctor_name=models.CharField(max_length=20,null=True)
	field=models.CharField(max_length=50,null=True)
	message=models.CharField(max_length=200,null=True)
	key=models.ForeignKey('patient_login.patient_login',models.DO_NOTHING) 

class patient_history(models.Model):
	height=models.CharField(max_length=10)
	weight=models.CharField(max_length=10)
	blood_group=models.CharField(max_length=10)
	previous_problem=models.CharField(max_length=10)
	height=models.CharField(max_length=10)
	status=models.CharField(max_length=15,default="filled")
	key=models.ForeignKey('patient_login.patient_login',models.DO_NOTHING) 


