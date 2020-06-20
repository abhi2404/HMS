from django.shortcuts import render,HttpResponse
import json 
from django.http import JsonResponse
from .models import login
from doctor_login.models import doctor_login

# Create your views here.
def index(request):
	if request.method == "POST":
		print(request.body)
		data=json.loads(request.body)
		username=data['email']
		password=data['password']
		bool_filter=login.objects.filter(email=username,password=password).exists()
		print(bool_filter)
		if (bool_filter):
			message=list(login.objects.filter(email=username).values('email'))   
		else:
			message="invalid credentials"	
	return JsonResponse(message,safe=False)


def dr_registration(request):
	if request.method == "GET":
		registration_list=list(doctor_login.objects.filter(status="pending").values('id','name','email','doctor_degree','mobile_no','status','field'))
	return JsonResponse(registration_list,safe=False)

def registration_accept(request):
	if request.method == "POST":
	    print(request.body)
	    data=json.loads(request.body)
	    Id=data['id']
	    doctor_login.objects.filter(id=Id).update(status="confirmed")
	    message="successfull"
	return JsonResponse(message,safe=False) 


def registration_reject(request):
	if request.method == "POST":
	    print(request.body)
	    data=json.loads(request.body)
	    Id=data['id']
	    doctor_login.objects.filter(id=Id).update(status="rejected")
	    message="successfull"
	return JsonResponse(message,safe=False)


def registration_approved(request):
	if request.method == "GET":
		registration_list=list(doctor_login.objects.filter(status="confirmed").values('id','name','email','doctor_degree','mobile_no','status','field'))
	return JsonResponse(registration_list,safe=False)
 
def registration_disapproved(request):
	if request.method == "GET":
		registration_list=list(doctor_login.objects.filter(status="rejected").values('id','name','email','doctor_degree','mobile_no','status','field'))
	return JsonResponse(registration_list,safe=False)   	