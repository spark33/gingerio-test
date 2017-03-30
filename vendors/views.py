from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Vendor
import datetime, operator

def index(request):

	vendors = Vendor.objects.all()
	last_month = datetime.date.today() - datetime.timedelta(days=30)
	recent_event_counts = map((lambda v: v.events.filter(start_time__gte=last_month).count()), Vendor.objects.all())
	vendor_list = list(zip(vendors, recent_event_counts))
	vendor_list.sort(key=operator.itemgetter(1), reverse=True)
	print(vendor_list)
	template = loader.get_template('vendors/index.html')
	context = {
		'vendor_list': vendor_list
	}
	return render(request, 'vendors/index.html', context)
  

def detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    return render(request, 'vendors/detail.html', {'vendor': vendor})
