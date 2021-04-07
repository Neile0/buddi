from django.core.files import File
from django.core.files.images import ImageFile
from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    return render(request, 'blog/index.html')


def news_detail(request, topic):
    detail = news.objects.get(topic=topic)

    read = detail.contend.readlines()

    print(detail.image.url)
    contextbox = {
        "topic" : detail.topic,
        "contend" : read,
        "pic" : detail.image.url
    }
    return render(request, "blog/news-detail.html", context=contextbox)
