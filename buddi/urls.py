from django.urls import path
from . import views

app_name = 'buddi'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user/<username>/', views.user_profile, name="user"),
    path('sitter/<username>/', views.sitter_profile, name="sitter"),
    path('become-a-buddi/', views.register, name='register'),
    path('find-sitter/', views.find_sitter, name='find-sitter'),
    ]

