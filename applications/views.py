from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Application

def applications_list(request):
    """View for applications list page."""
    # Create queryset ordered by date_applied.
    applications = Application.objects.order_by('-date_applied')
    # request is everything we recieve from the user via the internet.
    return render(request, 'applications/applications_list.html', {'applications': applications})

def application_detail(request, pk):
    """View for job application detail page."""
    application = get_object_or_404(Application, pk=pk)
    return render(request, 'applications/application_detail.html', {'application': application})
