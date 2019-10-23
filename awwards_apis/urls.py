from django.urls import path
from rest_framework import routers
from .views import *

urlpatterns = [
    path('API/users-details',profiles_api),
    path('API/posts-details',posts_api)
]
