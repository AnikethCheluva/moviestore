from django.contrib import admin
from .models import Movie, Review
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
admin.site.register(Movie, MovieAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['movie', 'source', 'user', 'date', 'reported']
    search_fields = ['movie__name', 'comment', 'source']
    list_filter = ['source']

admin.site.register(Review, ReviewAdmin)
# Register your models here.
