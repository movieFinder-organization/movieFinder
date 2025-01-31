from flask import render_template, request
from scripts.fetch_movie import fetch_random_movie, fetch_movie_details

@app.route('/', methods=['GET', 'POST'])
def index():
    movie_info = None
    if request.method == 'POST':
        genre = request.form.get('genre')
        year = request.form.get('year')
        movie = fetch_random_movie(genre, year)
        if movie:
            movie_info = fetch_movie_details(movie['title'])
    return render_template('index.html', movie_info=movie_info)