from django.shortcuts import render


#
# def get_parent_regions():
#     regions = Region.objects.filter(is_parent_region=True)
#     return [r for r in regions]


# Create your views here.

def index(request):
    # context_dict = {'regions': get_parent_regions()}
    return render(request, 'blog/index.html')


def show_article(request):
    #
    context_dict = {
        'title': None,
        'sub_title': None,
        'hero-image': None,
        'category': None,
        'author': None,
        'date_published': None,
        'date_edited': None,
    }
    return render(request, "blog/article.html", context=context_dict)


def news_detail(request, topic):
    detail = news.objects.get(topic=topic)

    read = detail.contend.readlines()

    print(detail.image.url)
    contextbox = {
        "topic": detail.topic,
        "contend": read,
        "pic": detail.image.url
    }
    return render(request, "blog/news-detail.html", context=contextbox)
