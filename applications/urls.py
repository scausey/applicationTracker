from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.applications_list, name='applications_list')
]
