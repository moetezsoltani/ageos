from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100, default='Unknown')  # Define default value here
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)  # New image field


    def __str__(self):
        return self.title

class Publication(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateField()
    author = models.CharField(max_length=100)  # Example field, adjust as per your actual model
    image = models.ImageField(upload_to='publication_images/', blank=True, null=True)  # New image field

class Formation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='formations_images/', blank=True, null=True)

    def __str__(self):
        return self.title
