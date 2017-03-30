from django.conf.urls import url

from . import views

app_name = 'vendors'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<vendor_id>[0-9]+)/$', views.detail, name='detail'),
]