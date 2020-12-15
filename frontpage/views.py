from django.shortcuts import render, HttpResponse

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