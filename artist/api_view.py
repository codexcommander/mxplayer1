from django.template.context_processors import request
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import *
from artist.models import *
from django.contrib.auth import get_user_model
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404

User = get_user_model()

class Dashboard_view(APIView):
    permission_classes = [IsAuthenticated]
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
    def post(self,request,email):
        user = get_object_or_404(User, email=email)
        data = request.data.copy()
        data['user'] = user.id
        serializer = PlaylistSerializer(data = request.data)
        if serializer.is_valid():
            playlist = serializer.save(user=user)
            return Response(PlaylistSerializer(playlist).data)
        else:
            return Response(serializer.errors)


class profile_view(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    def get(self,request,id):
        try:
            playlist = Playlist.objects.get(id=id)
            serializer = PlaylistSerializer(playlist)
            return Response(serializer.data)
        except Playlist.DoesNotExist:
            return Response({"error": "Playlist not found"})


    def delete(self,request,id):
        try:
            playlist = Playlist.objects.get(id=id)
            playlist.delete()
            return Response({"success": "Playlist deleted successfully"})

        except Playlist.DoesNotExist:
            return Response({"error": "Playlist not found"})
    def put(self,request,id):
        try:
            playlist = Playlist.objects.get(id=id)

            serializer = PlaylistSerializer(playlist,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except Playlist.DoesNotExist:
            return Response({"error": "Playlist not found"})

class Song_Playlist(APIView):
    def get(self,request,id):

        song = Song.objects.filter(playlist__id = id)
        serializer = SongSerializer(song,many=True)
        return Response(serializer.data)

class Song_album(APIView):
    def get(self,request,id):
        song = Song.objects.filter(album__id = id)
        serializer = SongSerializer(song,many=True)
        return Response(serializer.data)