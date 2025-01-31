import requests
import os
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv('TMDB_API_KEY')
OMDB_API_KEY = os.getenv('OMDB_API_KEY')

def fetch_random_movie(genre, year):
    """
    Fetch a random movie from TMDB based on genre and year.
    """
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres={genre}&year={year}"
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json().get('results', [])
        if movies:
            return movies[0]  # Return the first movie
    return None

def fetch_movie_details(title):
    """
    Fetch movie details from OMDB using the movie title.
    """
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={title}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None