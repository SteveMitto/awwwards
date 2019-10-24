from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('API/users-details',profiles_api),
    path('API/posts-details',posts_api),
    path('devops/',developer,name='developer'),
    path('get_api_key/',get_api_key)
]
