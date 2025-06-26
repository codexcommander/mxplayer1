from django.db import models
from user.models import Playlist



class Album(models.Model):
    name = models.CharField(max_length=120)
    cover = models.ImageField(upload_to='album_images',null=True,blank=True)

class Artist(models.Model):
    name = models.CharField(max_length=120)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)

class Song(models.Model):
    title = models.CharField(max_length=120)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    playlist = models.ManyToManyField(Playlist)
    genre = models.CharField(max_length=120)
    audio = models.FileField(upload_to='audio')
    upload_at = models.DateField(auto_now=True)




