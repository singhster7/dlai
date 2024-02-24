# views.py

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

from django.http import JsonResponse

def analytics_data(request):
       data = {
           'likes': 100,
           'shares': 50,
           'comments': 25
       }
       return JsonResponse(data)
