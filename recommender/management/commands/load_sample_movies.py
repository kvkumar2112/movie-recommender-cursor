from django.core.management.base import BaseCommand
from recommender.models import Movie
from datetime import date

class Command(BaseCommand):
    help = 'Loads sample movies into the database'

    def handle(self, *args, **options):
        sample_movies = [
            {
                'title': 'The Shawshank Redemption',
                'genre': 'Drama',
                'average_rating': 9.3,
                'description': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
                'release_date': date(1994, 9, 23)
            },
            {
                'title': 'The Godfather',
                'genre': 'Crime, Drama',
                'average_rating': 9.2,
                'description': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
                'release_date': date(1972, 3, 24)
            },
            {
                'title': 'The Dark Knight',
                'genre': 'Action, Crime, Drama',
                'average_rating': 9.0,
                'description': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
                'release_date': date(2008, 7, 18)
            },
            {
                'title': 'Pulp Fiction',
                'genre': 'Crime, Drama',
                'average_rating': 8.9,
                'description': 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
                'release_date': date(1994, 10, 14)
            },
            {
                'title': 'Inception',
                'genre': 'Action, Adventure, Sci-Fi',
                'average_rating': 8.8,
                'description': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.',
                'release_date': date(2010, 7, 16)
            },
            {
                'title': 'The Matrix',
                'genre': 'Action, Sci-Fi',
                'average_rating': 8.7,
                'description': 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.',
                'release_date': date(1999, 3, 31)
            },
            {
                'title': 'Forrest Gump',
                'genre': 'Drama, Romance',
                'average_rating': 8.8,
                'description': 'The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.',
                'release_date': date(1994, 7, 6)
            },
            {
                'title': 'The Lord of the Rings: The Fellowship of the Ring',
                'genre': 'Adventure, Fantasy',
                'average_rating': 8.8,
                'description': 'A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.',
                'release_date': date(2001, 12, 19)
            },
            {
                'title': 'Fight Club',
                'genre': 'Drama',
                'average_rating': 8.8,
                'description': 'An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more.',
                'release_date': date(1999, 10, 15)
            },
            {
                'title': 'Goodfellas',
                'genre': 'Biography, Crime, Drama',
                'average_rating': 8.7,
                'description': 'The story of Henry Hill and his life in the mob, covering his relationship with his wife and his mob partners and the ramifications of his lifestyle.',
                'release_date': date(1990, 9, 19)
            }
        ]

        for movie_data in sample_movies:
            movie, created = Movie.objects.get_or_create(
                title=movie_data['title'],
                defaults=movie_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created movie: {movie.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Movie already exists: {movie.title}')) 