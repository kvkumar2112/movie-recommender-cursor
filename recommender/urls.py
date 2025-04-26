from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('preferences/', views.set_preferences, name='preferences'),
    path('rate/<int:movie_id>/', views.rate_movie, name='rate_movie'),
] 