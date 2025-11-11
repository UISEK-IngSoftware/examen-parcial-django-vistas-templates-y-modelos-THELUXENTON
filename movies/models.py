from django.db import models

class Movie(models.Model):
  
    title = models.CharField(max_length=200) 
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    synopsis = models.TextField()
