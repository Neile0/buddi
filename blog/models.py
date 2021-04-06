from django.db import models
from datetime import datetime
NAME_MAX_LENGTH = 128


# Create your models here.
class shop(models.Model):
    topic = models.CharField(max_length=NAME_MAX_LENGTH)
    contend = models.FileField(upload_to='contend')
    image = models.FileField(upload_to='image')

class vet(models.Model):
    topic = models.CharField(max_length=NAME_MAX_LENGTH)
    contend = models.FileField(upload_to='contend')
    image = models.FileField(upload_to='image')

class news(models.Model):
    topic = models.CharField(max_length=NAME_MAX_LENGTH)
    contend = models.FileField(upload_to='contend')
    image = models.FileField(upload_to='image')
    date = models.DateTimeField(default=datetime.now(), editable=False)