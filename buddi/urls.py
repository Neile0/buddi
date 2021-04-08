from django.urls import path
from . import views

app_name = 'buddi'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/<case>/<place>/', views.search, name='search'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user/<username>/', views.user_profile, name="user"),
    path('add_pet/<username>/', views.add_pet, name="add_pet"),
    path('add_opreg/<username>/', views.add_opreg, name="add_opreg"),
    path('sitter/<username>/', views.sitter_profile, name="sitter"),
    path('delete/<animal_id>/', views.delete_animal, name="delete_animal"),
    path('delete/<sitteropreg_id>', views.delete_opregion, name="delete_opregion"),
    path('become-a-buddi/', views.register, name='register'),
    path('find-sitter/', views.find_sitter, name='find-sitter'),
    ]
