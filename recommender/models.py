from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    average_rating = models.FloatField()
    description = models.TextField()
    release_date = models.DateField()
    
    def __str__(self):
        return self.title

class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_genres = models.CharField(max_length=500, help_text="Comma-separated list of preferred genres")
    min_rating = models.FloatField(default=0.0)
    min_release_year = models.IntegerField(default=1900)
    
    def __str__(self):
        return f"{self.user.username}'s preferences"

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'movie')
    
    def __str__(self):
        return f"{self.user.username} rated {self.movie.title} {self.rating}"
