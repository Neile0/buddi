from django.urls import path
from . import views

app_name = 'buddi'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('become-a-buddi/', views.register, name='register'),
    path('find-sitter/', views.find_sitter, name='find-sitter'),
]
