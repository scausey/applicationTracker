from django import forms

from .models import Application

class AddApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('company', 'position', 'location', 'date_applied', 'status', 'notes')
