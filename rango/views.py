from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Review
from rango.models import Reviewer
from rango.models import Film
from rango.models import Rating
#from rango.forms import
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from datetime import datetime

from django.shortcuts import redirect
from django.contrib.auth.models import User
#from rango.models import UserProfile

# Create your views here.
def home(request):
    film_list = Film.objects.order_by('rating')[:5]
    review_list = Review.objects.order_by('-date')[:5]

    context_dict = {}

    context_dict['films'] = film_list
    context_dict['reviews'] = review_list

    response = render(request, 'home.html', context_dict)
    return response

def about(request):
    return render(request, 'about.html')

def show_film(request, film_name_slug):
    context_dict={}
    try:
        film = Film.objects.get(slug=film_name_slug)
        reviews = Review.objects.filter(fkID = film.filmID).order_by('-date')

        context_dict['film'] = film
        context_dict['reviews'] = reviews
    except Film.DoesNotExist:
        context_dict['film'] = None
        context_dict['reviews'] = None

    return render(request, 'film.html',context=context_dict)

def show_reviewer(request, reviewer_name_slug):
    context_dict={}
    try:
        reviewer = Reviewer.objects.get(slug=reviewer_name_slug)
        reviews = Review.objects.filter(reviewerID = reviewer).order_by('-date')

        context_dict['reviewer'] = reviewer
        context_dict['reviews'] = reviews
    except Review.DoesNotExist:
        context_dict['reviewer'] = None
        context_dict['reviews'] = None


    return render(request, 'reviewer.html', context=context_dict)