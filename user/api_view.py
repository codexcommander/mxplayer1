
from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomEmailTokenObtainPairSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer



@method_decorator(csrf_exempt, name='dispatch')

class CustomEmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomEmailTokenObtainPairSerializer

