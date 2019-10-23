from awwwards.models import Post,Profile,Country,Profession,Tag
from django.contrib.auth.models import User
from rest_framework import serializers as ser
# Create your models here.

Post=Post
Profile=Profile
class CountrySerializer(ser.ModelSerializer):
    class Meta:
        model =Country
        fields=['id','name','flags']

class ProfessionSerializer(ser.ModelSerializer):
    class Meta:
        model=Profession
        fields=['profession']

class PostSerializer(ser.ModelSerializer):
    class Meta:
        model = Post
        fields=['id','title','description','main_image']

class ProfileSerializer(ser.ModelSerializer):
    country = CountrySerializer(read_only=True)
    post = PostSerializer(read_only=True)
    class Meta:
        model =Profile
        fields=['id','profile_pic','country','bio','display_name','link','post']

class UserSerializer(ser.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    posts =PostSerializer(many=True)
    class Meta:
        model=User
        fields=['username','profile','posts']
