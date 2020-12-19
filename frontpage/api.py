from models import Submit
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
        def api_engine():
        """This Function will send the fields required for
        recommendation"""
        ins = Submit.objects.all()[-1]
        genres = ins.genre
        rating = ins.rating
        release_year = ins.Release_year
        actors = ins.cast
        url = 'https://api.themoviedb.org/3/discover/movie'
        params = {'language':'en','region':'','primary_release_year':'','with_cast':'','with_genres':[],'':'','':'','':'','':'' }
        r = requests.get(url, params=params)
        if r.status_code == 200:
            response = dict(r.json)
            movie_title = response["results"][sr_no]["original_title"]
            movie_genre = response["results"][sr_no]["genre_ids"]
            movie_rating = response["results"][sr_no]["vote_average"] 
            movie_year = response["results"][sr_no]["release_date"][0:4]
            movie_summary = response["results"][sr_no]["overview"]
        return movie_title, movie_genre, movie_rating, movie_year, movie_summary

    
    pass


    
    





def api_recieve():
    """
    This function will recieve the movies from movie api
    """
    pass


movie_title, movie_genre, movie_rating, movie_year, movie_summary = api_engine()
