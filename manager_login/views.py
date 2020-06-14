from django.shortcuts import render,HttpResponse
import json 
from django.http import JsonResponse
from .models import login

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
			message="ok"
		else:
			message="invalid credentials"	
	return JsonResponse(message,safe=False)