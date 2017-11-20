from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.applications_list, name='applications_list'),
    url(r'^jobapp/(?P<pk>\d+)/$', views.application_detail, name='application_detail'),
    url(r'^jobapp/new$', views.add_application, name='add_application'),
    url(r'^jobapp/(?P<pk>\d+)/edit/$', views.application_edit, name='application_edit'),
]
