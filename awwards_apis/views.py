from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from .serializers import *
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
import json
@login_required
def developer(request):
    return render(request,'developer.html')

@login_required
def get_api_key(request):
    user_token = Token.objects.get_or_create(user = request.user)
    my_token=None
    if user_token :
        for i in user_token:
            my_token= json.dumps(str(i))[1:-1]
            break
    context={
    'token':my_token
    }
    return JsonResponse(context)

@api_view(['GET','POST'])
def profiles_api(request):
    profiles = User.objects.all()
    serializer= UserSerializer(profiles,many =True)

    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def posts_api(request):
    query = Post.objects.all()
    serializer=PostMainSerializer(query,many=True)

    return JsonResponse(serializer.data,safe=False)
