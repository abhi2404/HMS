from django.db import models
from patient_details.models import patient_appointment

# Create your models here.
class payment(models.Model):
	link=models.ForeignKey('patient_details.patient_appointment',models.DO_NOTHING)
	doctor_name=models.CharField(max_length=20)
	payment_for=models.CharField(max_length=30)
	cost=models.CharField(max_length=7)

