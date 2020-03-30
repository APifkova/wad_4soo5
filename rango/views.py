from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Review
from rango.models import Reviewer
from rango.models import Film
from rango.models import Rating
from rango.forms import *
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.urls import reverse

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
    except Reviewer.DoesNotExist:
        context_dict['reviewer'] = None
        context_dict['reviews'] = None

    return render(request, 'reviewer.html', context=context_dict)

def add_reviewer(request,reviewer_name_slug):
    context_dict = {}
    form = ReviewerForm()
    if request.method=='POST':
        form = ReviewerForm(request.POST)
        if form.is_valid():

            reviewer = form.save(commit=False)
            reviewer.user = request.user
            reviewer.save()

            if 'profilePicture' in request.FILES:
                reviewer.profilePicture = request.FILES['profilePicture']

            reviewer.save()

            return redirect(reverse('rango:show_reviewer', kwargs={'reviewer_name_slug':reviewer_name_slug}))
        else:
            print(form.errors)

    context_dict['form'] = form

    return render(request, 'add_reviewer.html',  context = context_dict)

def add_film(request):
    context_dict = {}
    form = FilmForm()
    if request.method=='POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            film = form.save(commit=False)

            if 'poster' in request.FILES:
                film.poster = request.FILES['poster']

            film.save()

            return redirect(reverse('rango:show_film',kwargs={'film_name_slug':film.slug}))

        else:
            print(form.errors)

    context_dict['form'] = form

    return render(request, 'add_film.html', context = context_dict)

def add_review(request, film_name_slug):
    context_dict={}
    form = ReviewForm()
    try:
        film = Film.objects.get(slug = film_name_slug)
    except Film.DoesNotExist:
        film = None

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review=form.save(commit=False)
            review.reviewerID = request.user.reviewer
            review.fkID = film

            review.save()

            return redirect(reverse('rango:show_film', kwargs={'film_name_slug': film_name_slug}))

        else:
            print(form.errors)

    context_dict['form']=form
    context_dict['film']=film

    return render(request,'add_review.html',context=context_dict)