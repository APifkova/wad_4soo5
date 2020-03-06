from django.contrib import admin
from rango.models import Film, Review, Rating, User, Reviewer

# Register your models here.

admin.site.register(Film)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(User)
admin.site.register(Reviewer)
