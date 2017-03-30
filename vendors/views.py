from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Vendor

def index(request):
	vendor_list = Vendor.objects.all
	template = loader.get_template('vendors/index.html')
	context = {
		'vendor_list': vendor_list,
	}
	return render(request, 'vendors/index.html', context)
  

def detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    return render(request, 'vendors/detail.html', {'vendor': vendor})
