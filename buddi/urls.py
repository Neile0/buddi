from django.urls import path
from buddi import views

app_name = 'buddi'

urlpatters = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('become-a-buddi/', views.register, name='register'),
]
