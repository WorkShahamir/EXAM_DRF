"""
URL configuration for exam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from news.views import (
    NewsListCreateAPIView,
    NewsRetrieveUpdateDestroyAPIView,
    CommentListCreateAPIView,
    CommentRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('api/account/', include('account.urls')),
    path('api/news/', NewsListCreateAPIView.as_view()),
    path('api/news/<int:pk>/', NewsRetrieveUpdateDestroyAPIView.as_view()),
    path('api/news/<int:news_id>/comments/', CommentListCreateAPIView.as_view()),
    path('api/news/<int:news_id>/comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]

schema_view = get_schema_view(
    openapi.Info(
        title="News Portal API",
        default_version='v1',
        description="API documentation for News Portal",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns += [
    path('api/docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
