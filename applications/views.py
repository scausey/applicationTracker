from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Application
from .forms import AddApplicationForm


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

def add_application(request):
    if request.method == "POST":
        # Construct the AddApplicationForm with data from the form.
        form = AddApplicationForm(request.POST)
        if form.is_valid():
            post = form.save(commit="False")
            # Preserve changes and add a new application.
            post.save()
            return redirect('application_detail', pk=post.pk)
    else:
        form = AddApplicationForm()
    return render(request, 'applications/add_application.html', {'form': form})

def application_edit(request, pk):
    post = get_object_or_404(Application, pk=pk)
    if request.method == "POST":
        form = AddApplicationForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('application_detail', pk=post.pk)
    else:
        form = AddApplicationForm(instance=post)
    return render(request, 'applications/add_application.html', {'form': form})
