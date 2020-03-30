from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('film/<slug:film_name_slug>/', views.show_film, name='show_film'),
    path('film/<slug:film_name_slug>/add_review/', views.add_review, name='add_review'),
    path('user/<slug:reviewer_name_slug>/', views.show_reviewer, name='show_reviewer'),
    path('user/add_reviewer/<slug:reviewer_name_slug>/', views.add_reviewer, name='add_reviewer'),
    path('add_film/', views.add_film, name='add_film'),
]