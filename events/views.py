from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Event

def index(request):
	upcoming_events_list = Event.objects.order_by('-start_time')[:30]
	template = loader.get_template('events/index.html')
	context = {
		'upcoming_events_list': upcoming_events_list,
	}
	return render(request, 'events/index.html', context)
  

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/detail.html', {'event': event})
