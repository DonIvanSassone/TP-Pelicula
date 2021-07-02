from django.db import models
from django.utils import timezone


class FilmsToWatch(models.Model):
    Originalname = models.CharField(max_length = 200)
    Year = models.DateTimeField()
    Sinopsis = models.TextField()
    Director = models.CharField(max_length = 30)
    Duration = models.CharField(max_length = 6)
    Genres = models.CharField(max_length = 200)
    published_date = models.DateTimeField(
            blank=True, null=True)
    RATE_CHOICES = (
        (1,"1"),
        (2,"2"),
        (3,"3"),
        (4,"4"),
        (5,"5"),
    )
    rate = models.PositiveSmallIntegerField(choices = RATE_CHOICES, default = 0)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.Originalname
