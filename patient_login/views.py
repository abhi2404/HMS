from django.shortcuts import render,HttpResponse
import json 
from django.http import JsonResponse
from .models import patient_login

# Create your views here.
def signup(request):
	if request.method =="POST":
		print(request.body)
		data=json.loads(request.body)
		name=data['name']
		username=data['email']
		password=data['password']
		contact_no=data['contact_no']
		age=data['age']
		gender=data['gender']
		unique_email=patient_login.objects.filter(email=username).exists()
		if(unique_email):
			message ="This email is already registered"
		else:
			patient_login.objects.create(name=name,email=username,password=password,mobile_no=contact_no,age=age,gender=gender)
			message="Registration Successfull"
	return JsonResponse(message,safe=False)


def pt_login(request):
	if request.method == "POST":
		print(request.body)
		data=json.loads(request.body)
		username=data['email']
		password=data['password']
		bool_filter=patient_login.objects.filter(email=username,password=password).exists()  
		print(bool_filter)
		if (bool_filter):
			message=list(patient_login.objects.filter(email=username).values())
		else:
			message="invalid credentials"	
	return JsonResponse(message,safe=False)
