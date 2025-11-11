from django.shortcuts import render
from .models import Movie
from django.http import HttpResponse 

def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies_list': movies
    }
    return render(request, 'movies/index.html', context)


def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        
        context = {
            'movie': movie 
        }
        return render(request, 'movies/movie_detail.html', context)
        
    except Movie.DoesNotExist:
     
        return HttpResponse("<h1>Error: Película no encontrada</h1>", status=404)