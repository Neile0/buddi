from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'buddi'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name="search"),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('sitter/<username>/', views.sitter, name="sitter"),
    path('delete/<animal_id>/', views.delete_animal, name="delete_animal"),
    path('delete/<sitteropreg_id>', views.delete_opregion, name="delete_opregion"),
    path('become-a-buddi/', views.register, name='register'),
    path('find-sitter/', views.find_sitter, name='find-sitter'),
    url(r'^sit/(?P<param>.+)/$', views.sit, name='sit'),
    url(r'^sitters/(?P<param>.+)/$', views.sitters, name='sitters'),
    path('<username>/', views.user_profile, name="user"),
    path('<username>/add-buddi/', views.add_pet, name="add_pet"),
    path('<username>/where-to-operate', views.add_opreg, name="add_opreg"),
    path('<username>/change-profile-image', views.change_user_image, name="change_user_image"),
]
