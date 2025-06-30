from django.urls import path
from .api_view import *
from user.api_view import *
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('dashboard_api/<email>/',Dashboard_view.as_view(),name='dashboard_api'),

    path('profile_view/<email>/', profile_view.as_view(), name='profile_view'),
    path('Song_Playlist/<int:id>/', Song_Playlist.as_view(), name='Song_Playlist'),
    path('Song_album/<id>/', Song_album.as_view(), name='Song_album'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login_api/', CustomEmailTokenObtainPairView.as_view(), name='custom_email_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]