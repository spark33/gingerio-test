from django.db import models
from events.models import Event

# Create your models here.
class Vendor(models.Model):
	name = models.CharField(max_length=50)
	events = models.ManyToManyField(Event)
	description = models.CharField(max_length=200)

	def __str__(self):
		return self.name