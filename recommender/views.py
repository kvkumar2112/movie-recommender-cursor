from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Movie, UserPreference, Rating
from .forms import UserPreferenceForm, RatingForm
import logging

logger = logging.getLogger(__name__)

def home(request):
    movies = Movie.objects.all()
    logger.info(f"Total movies in database: {movies.count()}")
    
    # Apply filters if user is logged in and has preferences
    if request.user.is_authenticated:
        try:
            preferences = UserPreference.objects.get(user=request.user)
            logger.info(f"User preferences found: {preferences}")
            if preferences.preferred_genres:
                genres = [g.strip() for g in preferences.preferred_genres.split(',')]
                logger.info(f"Filtering by genres: {genres}")
                movies = movies.filter(genre__in=genres)
            movies = movies.filter(average_rating__gte=preferences.min_rating)
            movies = movies.filter(release_date__year__gte=preferences.min_release_year)
            logger.info(f"Movies after filtering: {movies.count()}")
        except UserPreference.DoesNotExist:
            logger.info("No user preferences found")
            pass
    
    logger.info(f"Final movies count: {movies.count()}")
    return render(request, 'recommender/home.html', {
        'movies': movies,
        'user_ratings': Rating.objects.filter(user=request.user) if request.user.is_authenticated else None
    })

@login_required
def set_preferences(request):
    try:
        preferences = UserPreference.objects.get(user=request.user)
    except UserPreference.DoesNotExist:
        preferences = None

    if request.method == 'POST':
        form = UserPreferenceForm(request.POST, instance=preferences)
        if form.is_valid():
            preferences = form.save(commit=False)
            preferences.user = request.user
            preferences.save()
            messages.success(request, 'Your preferences have been updated!')
            return redirect('home')
    else:
        form = UserPreferenceForm(instance=preferences)

    return render(request, 'recommender/preferences.html', {'form': form})

@login_required
def rate_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    try:
        rating = Rating.objects.get(user=request.user, movie=movie)
    except Rating.DoesNotExist:
        rating = None

    if request.method == 'POST':
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.movie = movie
            rating.save()
            
            # Update movie's average rating
            all_ratings = Rating.objects.filter(movie=movie)
            movie.average_rating = sum(r.rating for r in all_ratings) / all_ratings.count()
            movie.save()
            
            messages.success(request, f'You rated {movie.title} {rating.rating}/10')
            return redirect('home')
    else:
        form = RatingForm(instance=rating)

    return render(request, 'recommender/rate_movie.html', {
        'form': form,
        'movie': movie
    })
