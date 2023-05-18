from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import AuthorRegistrationSerializer
from .models import Author


class AuthorRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorRegistrationSerializer
