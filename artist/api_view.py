

from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from user.models import *
from artist.models import *
from django.contrib.auth import get_user_model
User = get_user_model()

class Dashboard_view(APIView):

    def get(self, request,email):
        user = User.objects.get(email=email)
        playlist = Playlist.objects.filter(user=user)
        user_data = UserSerializer(user).data
        albums = Album.objects.all()
        albums_data = AlbumSerializer(albums,many=True).data
        playlist_data = PlaylistSerializer(playlist,many=True).data

        return Response({
            "user": user_data,
            "songs": playlist_data,
            "albums" : albums_data
        })

class profile_view(APIView):

    def get(self,request,email):
        user = User.objects.get(email=email)
        user_data = UserSerializer(user).data
        return Response(user_data)
    def put(self,request,email):
        print(request.FILES.get('profile_img'))
        user = User.objects.get(email=email)
        serializer = UserSerializer(user,data= request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class playlist_view(APIView):
    def post(self,request):

        serializer = PlaylistSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

