from frontpage.models import Submit
import os
import requests
from dotenv import load_dotenv
#from tmdbv3api import TMDb, Discover

load_dotenv()

TOKEN = os.getenv('TMDB_API_KEY')

#https://api.themoviedb.org/3/discover/movie?api_key=fd7d4ef01b96e4f537a8198c4d6250b9&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=3&primary_release_year=2011&with_cast=Tom%20hanls&with_genres=action

class movie(object):
    """
    docstring
    """
    def api_engine(self):
        """This Function will send the fields required for
        recommendation"""'''
        con = sqlite3.connect('db.sqlite3')
        cur = con.cursor()
    
        last_row = cur.execute("SELECT * FROM table ORDER BY id DESC LIMIT 1")'''
        last_row = len(Submit.objects.all()) - 1
        ins = Submit.objects.all()[last_row]
        genres = ins.genre
        rating = ins.rating
        release_year = ins.Release_year
        #actors = last_row.cast
        #Submit.objects.all().delete()
        url = 'https://api.themoviedb.org/3/discover/movie'
        params = {'api_key':TOKEN, 'language':'en','primary_release_year':release_year,'with_genres':genres, 'vote_average.gte':rating,'sort_by': 'popularity.desc'}

        r = requests.get(url, params=params)
        title = []
        genre = []
        rating = []
        year = []
        summary = []
        if r.status_code == 200:
            response = r.json()
            no_of_movies = len(response["results"])
            
            for mov in range(no_of_movies):
                title.append(response["results"][mov]["original_title"])
                genre.append(response["results"][mov]["genre_ids"])
                rating.append(response["results"][mov]["vote_average"])
                year.append(response["results"][mov]["release_date"][0:4])
                summary.append(response["results"][mov]["overview"])
            return title, genre, rating, year, summary, no_of_movies
        else:
            return -1