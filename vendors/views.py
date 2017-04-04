from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Vendor
import datetime, operator

def index(request):

	vendors = Vendor.objects.all()
	last_month = datetime.date.today() - datetime.timedelta(days=30)
	recent_event_counts = map((lambda v: v.events.filter(start_time__gte=last_month).count()), Vendor.objects.all())
	vendor_list = list(zip(vendors, recent_event_counts))
	vendor_list.sort(key=operator.itemgetter(1), reverse=True)
	template = loader.get_template('vendors/index.html')

	paginator = Paginator(vendor_list, 10) # Show 10 vendors per page

	page = request.GET.get('page')
	try:
		vendors = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		vendors = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		vendors = paginator.page(paginator.num_pages)

	return render(request, 'vendors/index.html', {'vendors': vendors})
  

def detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    return render(request, 'vendors/detail.html', {'vendor': vendor})
