from django.db import models
from django.utils import timezone


class FilmsToWatch(models.Model):
    Original_name = models.CharField(max_length=200)
    Sinopsis = models.TextField()
    Year = models.DateTimeField(default=timezone.now)
