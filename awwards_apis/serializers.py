from awwwards.models import Post,Profile,Country,Profession,Tag,Rating
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
    profile = ProfileSerializer()
    posts =PostSerializer(many=True)
    class Meta:
        model=User
        fields=['username','profile','posts']

################     POSTS API        ################
class User2Serializer(ser.ModelSerializer):
    class Meta:
        model =User
        fields=['username']

class TagSerializer(ser.ModelSerializer):
    class Meta:
        model=Tag
        fields=['tags']

class RatingSerializer(ser.ModelSerializer):
    user =User2Serializer(read_only=True)
    class Meta:
        model =Rating
        fields = ['user','design','usability','content','creativity','avarage']

class PostMainSerializer(ser.ModelSerializer):
    tags=TagSerializer(many=True,read_only=True)
    ratings =RatingSerializer(many=True,read_only=True)
    user =User2Serializer(read_only=True)
    class Meta:
        model = Post
        fields=['user','title','description','tags','main_image','posted_on','link','ratings']
