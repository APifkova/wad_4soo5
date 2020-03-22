from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models import Avg

# Create your models here.
class Film(models.Model):
    filmID = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 128)
    director = models.CharField(max_length = 128)
    releaseDate = models.DateField()
    blurb = models.CharField(max_length = 512)
    poster = models.ImageField()

    slug = models.SlugField(unique = True, null = False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Film, self).save(*args, **kwargs)

    def rate(self):
        rec = Review.objects.values('fkID').annotate(Avg('rating'))

        for fkID in rec:
            if fkID['fkID'] == self.filmID:
                mod = Film.objects.get(filmID = fkID['fkID'])
                mod.rating = fkID['rating__avg']
                mod.save()
                return fkID['rating__avg']
        return 2.5

    score = property(rate)

    def __str__(self):
        return self.title

class User(AbstractUser):
    is_standard = models.BooleanField(default=False)
    is_reviewer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Rating(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    fkID = models.ForeignKey(Film, on_delete=models.CASCADE)
    rating = models.IntegerField(validators = [MinValueValidator(-2),MaxValueValidator(5)])


class Reviewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    displayName = models.CharField(max_length = 128)
    profilePicture = models.ImageField()

    def __str__(self):
        return self.displayName

class Review(models.Model):
    reviewerID = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    fkID = models.ForeignKey(Film, on_delete=models.CASCADE)
    mainBody = models.CharField(max_length = 1000)
    rating = models.IntegerField(validators = [MinValueValidator(0),MaxValueValidator(5)])
    date = models.DateTimeField()

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)




