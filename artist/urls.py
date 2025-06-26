from django.urls import path
from .api_view import *
urlpatterns = [
    path('dashboard_api/<email>',Dashboard_view.as_view(),name='dashboard_api'),

    path('profile_view/<email>', profile_view.as_view(), name='profile_view'),

]