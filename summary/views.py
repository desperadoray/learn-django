from django.shortcuts import render

from .models import Person
from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render, get_object_or_404

def index(request):
	all_Persons = Person.objects.all()
	#html = ''
	#for item in all_Persons:
	#	url = '/summary/' + str(item.id) + '/'
	#	html += '<a href = "' + url + '">' + item.name + '</a><br>'
	#template = loader.get_template('summary/index.html')
	context = {
		'all_persons': all_Persons,
	}
	#return HttpResponse(template.render(context,request))
	return render(request, 'summary/index.html', context)

def Person_detail(request, Person_id):
	#return HttpResponse("<h2>details for Person ID" + str(Person_id) +"</h2>")
	#try:
	#	person = Person.objects.get(pk = person_id)
	#except person.DoesNotExist:
	#	raise Http404("Person does not exist")
	person = get_object_or_404(Person, pk = Person_id)
	return render(request, 'summary/detail.html', {'Person' : person})