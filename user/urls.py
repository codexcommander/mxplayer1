from django.urls import path
from .views import log_in,sign_up,dash_board,log_out,playlist_list,search_list,profile_update,album_song_list
urlpatterns = [
    path('login/',log_in,name='user_login'),
    path('signup/', sign_up, name='user_signup'),
    path('dashboard/',dash_board,name='user_dashboard'),
    path('logout/',log_out,name='user_logout'),
    path('dashboard/playlist/<int:pk>/',playlist_list,name='play_list'),
    path('search/',search_list,name='search'),
    path('profile/<email>',profile_update,name='profile'),
    path('album/<id>',album_song_list,name='album'),
]