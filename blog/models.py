from django.core.files.storage import FileSystemStorage
from django.db import models
from django.template.defaultfilters import slugify

fs = FileSystemStorage(location='/blog/articles/')

from django.utils import timezone

NAME_MAX_LENGTH = 120
TITLE_MAX_LENGTH = 120


class Article(models.Model):
    def upload(self, name):
        return '{0}/{1}'.format(slugify(self.date_published), name)

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    sub_title = models.CharField(max_length=TITLE_MAX_LENGTH, null=True)
    category = models.CharField(max_length=TITLE_MAX_LENGTH)
    hero_image = models.ImageField(storage=fs, upload_to=upload)
    author = models.CharField(max_length=NAME_MAX_LENGTH)
    date_published = models.DateTimeField()
    date_edited = models.DateTimeField(null=True)
    content = models.FileField(storage=fs, upload_to=upload)
    is_published = models.BooleanField(default=True)


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
