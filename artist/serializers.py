from rest_framework import serializers
from .models import Album, Artist, Song
from user.models import Playlist
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'profile_img': {'required': False}}

class PlaylistSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Playlist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(read_only=True)

    class Meta:
        model = Artist
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    album = AlbumSerializer(read_only=True)
    playlist = PlaylistSerializer(many=True, read_only=True)

    class Meta:
        model = Song
        fields = '__all__'
