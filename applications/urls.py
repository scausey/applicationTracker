from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.applications_list, name='applications_list'),
    url(r'^jobapp/(?P<pk>\d+)/$', views.application_detail, name='application_detail'),
]
