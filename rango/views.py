from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Review
from rango.models import Reviewer
from rango.models import Film
from rango.models import Rating

# Create your views here.
def home(request):
    film_list = Film.objects.order_by('score')[:5]
    review_list = Review.objects.order_by('releaseDate')[:5]