from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
	return HttpResponse("<h1>Summary</h1>")

def Person_detail(request, Person_id):
	return HttpResponse("<h2>details for Person ID" + str(Person_id) +"</h2>")