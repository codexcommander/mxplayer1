from user.models import Playlist

def user_info(request):
    if request.user.is_authenticated:
        user_name = request.user.email
        playlist_lists = Playlist.objects.filter(user__email=user_name)
        playlist_list = []
        for list in playlist_lists:
            playlist = list
            playlist_list.append(playlist)
        return {
            'user':request.user,
            'playlist': playlist_list,

        }
    return {}