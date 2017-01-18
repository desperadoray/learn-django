from django.shortcuts import render

from .models import Person
from django.http import HttpResponse
def index(request):
	all_Persons = Person.objects.all()
	html = ''
	for item in all_Persons:
		url = '/summary/' + str(item.id) + '/'
		html += '<a href = "' + url + '">' + item.name + '</a><br>'
	return HttpResponse(html)

def Person_detail(request, Person_id):
	return HttpResponse("<h2>details for Person ID" + str(Person_id) +"</h2>")