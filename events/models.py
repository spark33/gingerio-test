from django.db import models

class Event(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	location = models.CharField(max_length=200)

	def __str__(self):
		return self.name
