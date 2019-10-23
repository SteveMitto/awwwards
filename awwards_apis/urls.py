from django.urls import path
from rest_framework import routers
from .views import *

urlpatterns = [
    path('API/users-details',profiles_api)
]
