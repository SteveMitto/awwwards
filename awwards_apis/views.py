from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def profiles_api(request):
    profiles = User.objects.all()
    serializer= UserSerializer(profiles,many =True)

    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def posts_api(request):
    query = Post.objects.all()
    serializer=PostMainSerializer(query,many=True)

    return JsonResponse(serializer.data,safe=False)
