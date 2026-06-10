from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('animals/', views.animal_list, name='animal_list'),
    path('animals/<int:animal_id>/', views.animal_detail, name='animal_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
]