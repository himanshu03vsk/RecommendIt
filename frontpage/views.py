from django.shortcuts import render, HttpResponse
from frontpage.models import Submit
from frontpage.api import movie

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
        genre = request.POST.getlist('genre')
        Release_year = request.POST.get('Release_year')
        rating = request.POST.get('rating')
        cast = request.POST.get('cast')
        choice = Submit(genre=genre, Release_year=Release_year, rating=rating, cast=cast)
        choice.save()
    instance = movie()
    movie_title, movie_genre, movie_rating, movie_year, movie_summary, no_of_movies = instance.api_engine()
    context = {'title': movie_title, 'no_of_movies': range(no_of_movies), 'genre': movie_genre, 'rating': movie_rating, 'year': movie_year, 'summary': movie_summary}
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