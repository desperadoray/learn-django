from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length = 200)
	gender = models.CharField(max_length = 200)
	relation = models.CharField(max_length = 200)
	def __str__(self):
		return self.name + ' - ' + self.relation
class Event(models.Model):
	person = models.ForeignKey(Person, on_delete = models.CASCADE)
	event_name = models.CharField(max_length = 200)

	def __str__(self):
		return self.event_name