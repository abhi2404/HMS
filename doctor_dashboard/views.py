from django.shortcuts import render,HttpResponse
import json
from django.http import JsonResponse
from patient_login.models import patient_login
from patient_details.models import patient_appointment , patient_history 
from .models import report_form
from django.db.models import Count

# Create your views here.

def show_appointment_doctor(request):  #appointment deatils
	if request.method == "POST":
		print(request.body)
		data=json.loads(request.body)
		doctor_name=data['name']
		bool_filter=patient_appointment.objects.filter(status="forwarded",doctor_name=doctor_name).exists()
		print(bool_filter)
		if (bool_filter):
			message=list(patient_appointment.objects.filter(status="forwarded",doctor_name=doctor_name).values('id','key__name'))
		else:
			message="You have no appointments"	
	return JsonResponse(message,safe=False)

def show_appointment_id(request): #patientparticularlist
	if request.method == "POST":
		print(request.body)
		data=json.loads(request.body)
		Id=data['id']
		message=list(patient_appointment.objects.filter(id=Id).values('id','booking_date','date_of_appointment','time_of_appointment','problem','key__name','key_id'))
	return JsonResponse(message,safe=False)


def appointment_accept(request):
    if request.method =="POST":
       print(request.body)
       data=json.loads(request.body)
       Id=data['id']
       patient_appointment.objects.filter(id=Id).update(status="confirmed")
       message="confirmed"
    return JsonResponse(message,safe=False)

#reject feature alredy included in mangaer dashboard
#not call it again , using same url at doctor_end

def modify_appointment(request):
    if request.method =="POST":
       print(request.body)
       data=json.loads(request.body)
       Id=data['id']
       date_of_appointment=data['date']
       time_of_appointment=data['time']
       patient_appointment.objects.filter(id=Id).update(status="modified confirmed",date_of_appointment=date_of_appointment,time_of_appointment=time_of_appointment)
       message="Modified appointment"
    return JsonResponse(message,safe=False)


def show_appointment_confirm(request):  #appointment deatils confirmed
	if request.method == "POST":
		print(request.body)
		data=json.loads(request.body)
		doctor_name=data['name']
		bool_filter=patient_appointment.objects.filter(status="confirmed",doctor_name=doctor_name).exists()
		print(bool_filter)
		if (bool_filter):
			message=list(patient_appointment.objects.filter(status="confirmed",doctor_name=doctor_name).values('id','key__name','booking_date','date_of_appointment','time_of_appointment','problem','key_id'))
		else:
			message="You have no appointments"    
	return JsonResponse(message,safe=False)


def show_medical_history(request):
	if request.method =="POST":
		print(request.body)
		data=json.loads(request.body)
		try:
			Id=data['key_id']
			message= list(patient_history.objects.filter(key_id=Id).values('height','weight','blood_group','previous_problem'))
		except:
			message="No Medical History"	
	return JsonResponse(message,safe=False)


def report(request):
    if 	request.method =="POST":
    	print(request.body)
    	data=json.loads(request.body)
    	bp=data['bp']
    	SpO2=data['SpO2']
    	prescription=data['prescription']
    	Id=data['id']
    	try:
    		message=data['message']
    		report_form.objects.create(bp=bp,SpO2=SpO2,prescription=prescription,message=message,link=patient_appointment.objects.get(pk=Id))
    	except:
    		report_form.objects.create(bp=bp,SpO2=SpO2,prescription=prescription,link=patient_appointment.objects.get(pk=Id))
    	patient_appointment.objects.filter(id=Id).update(status="finished")		
    	response="Report Generated"
    return JsonResponse(response,safe=False)


def count(request):
	if request.method == "POST":
		print(request.body)
		data=json.loads(request.body)
		doctor_name=data['doctor_name']
		count=list(patient_appointment.objects.filter(status="finished",doctor_name=doctor_name).values('key_id').annotate(Count('id')))
		print(count)
		try:
			key_id=count[0]['key_id']
			print(key_id)
			message=list(patient_login.objects.filter(id=key_id).values())
		except:
			message="NONE"
	return JsonResponse(message,safe=False)
















    

