from django.urls import path
from .views import AuthorRegistrationAPIView

urlpatterns = [
    path('register/', AuthorRegistrationAPIView.as_view()),
]
