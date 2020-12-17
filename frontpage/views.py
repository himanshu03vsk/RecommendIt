from django.shortcuts import render, HttpResponse
from frontpage.models import Submit

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
    return render(request, 'results.html')
    # return HttpResponse("This is the movie you should watch!") 

def submit_form(request):
    if request.method == "POST":
        genre = request.POST.get('genre')
        Release_year = request.POST.get('Release_year')
        rating = request.POST.get('rating')
        cast = request.POST.get('cast')
        choice = Submit(genre=genre, Release_year=Release_year, rating=rating, cast=cast)
        choice.save()
    
    return render(request, 'submit-form.html')
