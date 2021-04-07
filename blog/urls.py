from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    path("<str:topic>", views.news_detail, name='news')
]
