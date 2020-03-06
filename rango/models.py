from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Film(models.Model):
    filmID = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 128)
    director = models.CharField(max_length = 128)
    releaseDate = models.DateField()
    blurb = models.CharField(max_length = 512)
    rating = models.DecimalField(decimal_places = 2, max_digits = 2, validators = [MinValueValidator(0),MaxValueValidator(5)])
    poster = models.ImageField()


class Rating(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    filmID = models.ForeignKey(Film, on_delete=models.CASCADE)
    rating = models.IntegerField(validators = [MinValueValidator(0),MaxValueValidator(5)])

class User(AbstractUser):
    is_standard = models.BooleanField(default=False)
    is_reviewer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class Reviewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    displayName = models.CharField(max_length = 128)
    profilePicture = models.ImageField()

class Review(models.Model):
    reviewerID = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    filmID = models.ForeignKey(Film, on_delete=models.CASCADE)
    mainBody = models.CharField(max_length = 1000)
    rating = models.IntegerField(validators = [MinValueValidator(0),MaxValueValidator(5)])
    date = models.DateTimeField()




