from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('film/<slug:film_name_slug>/', views.show_film, name='show_film'),
    path('user/<slug:reviewer_name_slug>/', views.show_reviewer, name='show_reviewer'),
]