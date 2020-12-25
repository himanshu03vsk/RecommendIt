from django.shortcuts import render, HttpResponse
from frontpage.models import Submit
import os
import requests
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('TMDB_API_KEY')

# Create your views here.
def index(request):
    return render(request, 'homepage.html')
    # return HttpResponse("This is Frontpage's Index")

def about(request):
    return HttpResponse("This is all about Develpers")

def start(request):
    return render(request, 'start.html')
    # return HttpResponse("Starting Recommending Process...Beep Boop")

def results(request):
    if request.method == "POST":
        movies_to_show = int(request.POST.get('amount'))
        pages_to_show = int(movies_to_show/12) + 1
        get_r18 = request.POST.getlist('r18')
        get_genres = request.POST.getlist('genre')
        get_release_year = request.POST.get('Release_year')
        get_rating = request.POST.get('rating')
        # get_cast = request.POST.get('cast')
        #actors = last_row.cast
        #Submit.objects.all().delete()
        url = 'https://api.themoviedb.org/3/discover/movie'
        r18 = []
        genre_names = {28: 'Action', 12:'Adventure',16:'Animation',35:'Comedy',80:'Crime', 99:'Documentry',
                      18:'Drama', 10751:'Family', 14:'Fantasy',36:'History',27:'Horror', 10402:'Music', 9648:'Mystry',
                      10749:'Romance', 878: 'Sci-Fi', 10770:'TV Movie', 53:'Thriller', 10752:'War', 37:'Western'}
        title = []
        genre = []
        rating = []
        year = []
        album = []
        summary = []
        no_of_movies = 0
        for i in range(pages_to_show):
            params = {'api_key':TOKEN,'page': i, 'language':'en','primary_release_date.gte':get_release_year,'include_adult': get_r18, 'with_genres':get_genres, 'vote_average.gte':get_rating,'sort_by': 'popularity.desc'}
            r = requests.get(url, params=params)
            if r.status_code == 200:
                response = r.json()
                counter = len(response["results"])
                no_of_movies += len(response["results"])
                for mov in range(counter):
                    path = response["results"][mov]["backdrop_path"]
                    album_path = f'https://image.tmdb.org/t/p/w500{path}'
                    r18.append(response["results"][mov]["adult"])
                    album.append(album_path)
                    title.append(response["results"][mov]["original_title"]+f' ({response["results"][mov]["release_date"][0:4]})')
                    ids = response["results"][mov]["genre_ids"]
                    if len(ids) > 1:
                        temp_list = []
                        for genrename in ids:
                            temp_list.append(genre_names.get(genrename))
                        genre.append(temp_list)
                    else:
                        genre.append(genre_names.get(ids[0]))
                    rating.append(response["results"][mov]["vote_average"])
                    
                    summary.append(response["results"][mov]["overview"])
    context = {'title': title, 'adult': r18, 'album' : album, 'no_of_movies': range(no_of_movies), 'genre': genre, 'rating': rating, 'year': year, 'summary': summary}
    return render(request, 'results.html', context)
    # return HttpResponse("This is the movie you should watch!") 

'''def submit_form(request):
    if request.method == "POST":
        genre = request.POST.getlist('genre')
        Release_year = request.POST.get('Release_year')
        rating = request.POST.get('rating')
        cast = request.POST.get('cast')
        choice = Submit(genre=genre, Release_year=Release_year, rating=rating, cast=cast)
        choice.save()
    
    return render(request, 'submit-form.html')
'''