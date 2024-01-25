from django.db import models

class EventsModel(models.Model):
    image = models.ImageField(upload_to='events')
    date = models.DateField()
    location_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.location_name

    class Meta:
        verbose_name_plural = "Events"
        verbose_name = 'Event'