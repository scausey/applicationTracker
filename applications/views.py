from django.utils import timezone
from django.shortcuts import render
from .models import Application

def applications_list(request):
    # Create queryset ordered by date_applied.
    applications = Application.objects.order_by('-date_applied')
    # request is everything we recieve from the user via the internet.
    return render(request, 'applications/applications_list.html', {'applications': applications})
