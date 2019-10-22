from django.contrib import admin

from .models import Image ,Contributor ,Profile, Profession ,Country, Tag, Post, Rating, Follow, Like,Sotd


admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Profession)
admin.site.register(Country)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Contributor)
admin.site.register(Rating)
admin.site.register(Follow)
admin.site.register(Like)
admin.site.register(Sotd)
