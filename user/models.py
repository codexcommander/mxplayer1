from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import NullIf

from .manager import UserManager


class CustomUser(AbstractUser):
     phone_no = models.CharField(max_length=12,unique=True)
     email = models.EmailField(unique=True)
     profile_img = models.ImageField(upload_to="profile_image")
     #playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE,default=1)
     username = None
     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS = ['phone_no']
     objects = UserManager()

from django.contrib.auth import get_user_model
User = get_user_model()
class Playlist(models.Model):
     name = models.CharField(max_length=120)
     user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)








