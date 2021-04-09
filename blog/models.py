from django.core.files.storage import FileSystemStorage
from django.db import models
from django.template.defaultfilters import slugify

fs = FileSystemStorage(location='/blog/articles/')

from django.utils import timezone

NAME_MAX_LENGTH = 120
TITLE_MAX_LENGTH = 120


class Category(models.Model):
    name = models.CharField(max_length=TITLE_MAX_LENGTH)


class Article(models.Model):
    def upload(self, name):
        return '{0}/{1}'.format(slugify(self.date_published), name)

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    sub_title = models.CharField(max_length=TITLE_MAX_LENGTH, null=True, blank=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    hero_image = models.ImageField(storage=fs, upload_to=upload)
    content = models.FileField(storage=fs, upload_to=upload)
    author = models.CharField(max_length=NAME_MAX_LENGTH)
    date_published = models.DateTimeField()
    date_last_edited = models.DateTimeField(null=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)


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
