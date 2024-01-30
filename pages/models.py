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


class FeedbacksModel(models.Model):
    image = models.ImageField(upload_to='feedbacks')
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Feedbacks"
        verbose_name = 'Feedback'


class EmailModel(models.Model):
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Emails"
        verbose_name = 'Email'


class OrderModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    total_people = models.PositiveSmallIntegerField()
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=100)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Orders"
        verbose_name = 'Order'
