from django.shortcuts import render,HttpResponse
import json
from django.http import JsonResponse
from patient_login.models import patient_login
from patient_details.models import patient_appointment , patient_history  
from doctor_login.models import doctor_login 
# Create your views here.

def show_details(request): #patientdetails
	if request.method =="GET":
		message=list(patient_login.objects.values('id','name','email','mobile_no','age','gender'))
	return JsonResponse(message,safe=False)

def show_appointment(request):  #appointment deatils
	if request.method == "GET":
		message=list(patient_appointment.objects.filter(status="pending").values('id','key__name'))
	return JsonResponse(message,safe=False)

#particular deatails
def show_appointment_id(request): #patientparticularlist
	if request.method == "POST":
		print(request.body)
		data=json.loads(request.body)
		Id=data['id']
		message=list(patient_appointment.objects.filter(id=Id).values('id','booking_date','date_of_appointment','time_of_appointment','fees','problem','status','key__name','key_id'))
	return JsonResponse(message,safe=False)

def send_doctor_list(request):  #dropdown
    if request.method =="GET":
    	print(request)
    	data=request.GET.get('field')
    	print(data)
    	message=doctor_login.objects.filter(field=data).values('name')
    return JsonResponse(list(message),safe=False)	
		
def forward_appointment(request):
    if request.method =="POST":
       print(request.body)
       data=json.loads(request.body)
       Id=data['id']
       name=data['name']
       field=data['field']
       patient_appointment.objects.filter(id=Id).update(status="forwarded",doctor_name=name,field=field)
       message="forwarded"
    return JsonResponse(message,safe=False)
 
def reject_appointment(request):
	if request.method == "POST":
		print(request.body)
		data=json.loads(request.body)
		Id=data['id']
		try:
			rejected_message=data['message']
			patient_appointment.objects.filter(id=Id).update(status="rejected",message=rejected_message)
			message="rejected"
		except:
			message="Fill the message field"
	return JsonResponse(message,safe=False)	
