from django.shortcuts import render,HttpResponse
import json
from django.http import JsonResponse
from .models import patient_appointment , patient_history
from patient_login.models import patient_login
from manager_dashboard.models import payment
from doctor_dashboard.models import report_form

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
		history=patient_history.objects.filter(status="filled",key_id=Id).exists()
		if history:
			patient_appointment.objects.create(date_of_appointment=date_of_appointment,time_of_appointment=time_of_appointment,problem=problem,fees=fees,key=patient_login.objects.get(pk=Id))
			message="status pending"
		else:
			message="Fill medical history first"
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


def show_fees(request):
    if request.method =="GET":
        data=request.GET.get('key_id')
        message=list(patient_appointment.objects.filter(key_id=data).values('fees','doctor_name','problem','date_of_appointment','time_of_appointment'))
    return JsonResponse(message,safe=False)


def test_cost(request):
	if request.method == "GET":
		data=request.GET.get('key_id')
		try:
			message=list(payment.objects.filter(link__key_id=data).values('doctor_name','payment_for','cost','link__date_of_appointment','link__time_of_appointment'))
		except:
			message="No Test yet"
	return JsonResponse(message,safe=False)


def prescription(request):
	if request.method== "GET":
		data=request.GET.get('key_id')
		message=list(report_form.objects.filter(link__key_id=data,link__status="finished").values('link__date_of_appointment'))
	return JsonResponse(message,safe=False)

def detail_report(request):
    if request.method =="POST":
    	print(request.body)
    	data=json.loads(request.body)
    	date=data['selected_date']
    	try:
    		message=list(report_form.objects.filter(link__date_of_appointment=date).values('bp','SpO2','prescription','message'))
    	except:
    		message="NOT YET GENERATED"
    return JsonResponse(message,safe=False)	

 
def notification(request):
	if request.method =="GET":
		Id=request.GET.get('id')
		message=list(patient_appointment.objects.filter(key_id=Id,notification="show").exclude(message=None).values('message','date_of_appointment','status'))
		if message==[]:
			return JsonResponse("NO",safe=False)
		else: 
			return JsonResponse(message,safe=False)

def remove(request):
	if request.method =="GET":
		Id=request.GET.get('id')
		patient_appointment.objects.filter(key_id=Id).exclude(status="pending").update(notification="dismiss")
	return JsonResponse("NO",safe=False)