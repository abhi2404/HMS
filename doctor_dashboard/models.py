from django.db import models
from patient_details.models import patient_appointment

# Create your models here.
class report_form(models.Model):
	bp=models.CharField(max_length=20)
	SpO2=models.CharField(max_length=5)
	prescription=models.CharField(max_length=300)
	message=models.CharField(max_length=100,null=True)
	link=models.ForeignKey('patient_details.patient_appointment',models.DO_NOTHING)

