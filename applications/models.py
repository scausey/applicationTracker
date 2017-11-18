import datetime
from django.db import models


class Application(models.Model):
    """Representation of a single job application."""
    company = models.CharField(max_length=200)
    #TODO: Add a url feild linking to the job description.
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date_applied = models.DateField(default=datetime.date.today)
    status = models.CharField(max_length=200)
    notes = models.TextField()

    def __str__(self):
        """Returns company and position."""
        company_position = "({}) {}".format( (self.company.upper()), self.position)
        return company_position
