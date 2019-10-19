from django.contrib import admin

from .models import Profile, Profession ,Country, Tag, Post, Rating, Follow, Like


admin.site.register(Profile)
admin.site.register(Profession)
admin.site.register(Country)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Rating)
admin.site.register(Follow)
admin.site.register(Like)
