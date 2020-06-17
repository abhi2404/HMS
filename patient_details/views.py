from django.shortcuts import render,HttpResponse
import json
from django.http import JsonResponse
from .models import patient_appointment , patient_history
from patient_login.models import patient_login

# Create your views here.
def apt(request):
	if request.method =="POST":
		print(request.body)
		data=json.loads(request.body)
		date_of_appointment=data['date_of_appointment']
		time_of_appointment=data['time_of_appointment']
		problem=data['problem']
		fees=data['fees']
		Id=data['id']
		patient_appointment.objects.create(date_of_appointment=date_of_appointment,time_of_appointment=time_of_appointment,problem=problem,fees=fees,key=patient_login.objects.get(pk=Id))
		message="status pending"
	return JsonResponse(message,safe=False)

def display_apt(request):
	if request.method =="GET":
		print(request)
		data=request.GET.get('id')
		print(data)
		message=patient_appointment.objects.filter(key_id=data).values('id','booking_date','date_of_appointment','time_of_appointment','status','fees')
	return JsonResponse(list(message),safe=False)

def medical_history(request):
	if request.method =="POST":
		print(request.body)
		data=json.loads(request.body)
		Id=data['id']
		height=data['height']
		weight=data['weight']
		blood_group=data['blood_group']
		previous_problem=data['previous_problem']
		filter_history=patient_history.objects.filter(key_id=Id,status="filled").exists()
		if filter_history:
			message="You have already filled once" 
		else:
			patient_history.objects.create(height=height,weight=weight,blood_group=blood_group,previous_problem=previous_problem,key=patient_login.objects.get(pk=Id))
			message="Updated Successfully"
	return JsonResponse(message,safe=False)


def display_history(request):
	if request.method =="GET":
		print(request)
		data=request.GET.get('id')
		print(data)
		message=patient_history.objects.filter(status="filled",key_id=data).values('height','weight','blood_group','previous_problem')
	return JsonResponse(list(message),safe=False)  
