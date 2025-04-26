from django.contrib import admin
from .models import Movie, UserPreference, Rating

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'average_rating', 'release_date')
    search_fields = ('title', 'genre')
    list_filter = ('genre', 'release_date')

@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'preferred_genres', 'min_rating', 'min_release_year')
    search_fields = ('user__username', 'preferred_genres')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'rating', 'created_at')
    search_fields = ('user__username', 'movie__title')
    list_filter = ('rating', 'created_at')
