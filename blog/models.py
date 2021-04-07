from django.db import models

from django.utils import timezone
NAME_MAX_LENGTH = 128


# Create your models here.
class shop(models.Model):
    topic = models.CharField(max_length=NAME_MAX_LENGTH)
    contend = models.FileField(upload_to='blog/contend')
    image = models.ImageField(upload_to='blog/image')

    def __str__(self):
        return self.topic

class vet(models.Model):
    topic = models.CharField(max_length=NAME_MAX_LENGTH)
    contend = models.FileField(upload_to='blog/contend')
    image = models.ImageField(upload_to='blog/image')

    def __str__(self):
        return self.topic

class news(models.Model):
    topic = models.CharField(max_length=NAME_MAX_LENGTH)
    contend = models.FileField(upload_to='blog/contend')
    image = models.ImageField(upload_to='blog/image')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.topic