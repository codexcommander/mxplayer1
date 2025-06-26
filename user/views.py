
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model, authenticate,login,logout
from user.models import Playlist
from django.contrib.auth.decorators import login_required
from artist.models import *
from django.db.models import Q
from django.http import JsonResponse, HttpResponse

User = get_user_model()
# Create your views here.

def sign_up(request):
    if request.method == "POST":
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(email = email)
        if not user_obj.exists():
            user_obj = User.objects.create(email=email,phone_no=phone_no)
            user_obj.set_password(password)
            user_obj.save()
            return redirect("user_login")
    return render(request, 'signup.html')

def log_in(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(email=email)
        if not user_obj.exists():
            return redirect('user_login')
        else:
            user_obj = authenticate(email=email,password=password)
            if not user_obj:
                return redirect('user_login')
            else:
                login(request,user_obj)
                return redirect('user_dashboard')
    return render(request,'login.html')

@login_required(login_url='/login/')
def log_out(request):
    logout(request)
    return redirect('user_login')


@login_required(login_url='/login/')
def dash_board(request):
    if request.method == "GET":
        email = request.GET.get('email')
        user_objs = User.objects.filter(email=email)
        albums = Album.objects.all()
        playlist_list = []
        names = []
        images = []
        user_name = request.user.email
        playlist_lists = Playlist.objects.filter(user__email=user_name)
        for list in playlist_lists:
            playlist = list
            playlist_list.append(playlist)
        for album in albums:
            name = album.name
            image = album.cover
            images.append(image)
            names.append(name)
        context = {
            'email' : user_name,
            'playlist' : playlist_list,
            'album' : albums
            }


    return render(request, 'dashboard.html',context)

@login_required(login_url='/login/')
def playlist_list(request,pk):
    if request.method == "GET":
        songs = Song.objects.filter(playlist =pk)
        names =[]
        song_audios =[]
        for song in songs:
            name = song.title
            song_audio = song.audio
            names.append(name)
            song_audios.append(song_audio)
        context = {
            'names' :names,
            'audio' : song_audios,
            'songs' : songs
        }
        return render(request,'playlist.html',context)

@login_required(login_url='/login/')
def search_list(request):
    search = request.GET.get('search')
    if search:
        results = Song.objects.filter(Q(title__icontains=search) | Q(artist__name__icontains=search) | Q(album__name__icontains=search))
        context = {
            'search_list' : results
        }
        print(results)
        return render(request,'search.html',context)
        #return JsonResponse(results)


@login_required(login_url='/login/')
def profile_update(request,email):
    if request.method == 'POST':
        try:
            user_obj = User.objects.get(email = email)
            user_obj.profile_img = request.FILES['profile_img']
            user_obj.phone_no = request.POST['phone_no']
            user_obj.save()
        except User.DoestNotExist:
            return HttpResponse("object not found",status=404)
    return  render(request,'profile.html')

@login_required(login_url='/login/')
def album_song_list(request,id):
    song_obj = Song.objects.filter(album=id)
    context ={
        'song_obj' : song_obj
    }
    return render(request,'song.html',context)


















































































































































































































































