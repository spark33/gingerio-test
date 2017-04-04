from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Event

def index(request):
	upcoming_events_list = Event.objects.all().order_by('-start_time')
	template = loader.get_template('events/index.html')
	paginator = Paginator(upcoming_events_list, 10) # Show 10 events per page

	page = request.GET.get('page')
	try:
		events = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		events = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		events = paginator.page(paginator.num_pages)

	return render(request, 'events/index.html', {'events': events})
  

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/detail.html', {'event': event})
