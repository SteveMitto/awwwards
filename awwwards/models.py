from django.db import models as md
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profession(md.Model):
    profession = md.CharField(max_length=100)

    class Meta:
        ordering=['profession']

    def __str__(self):
        return f'{self.profession}'
class Profile(md.Model):
    user = md.OneToOneField(User,on_delete=md.PROTECT)
    profile_pic= md.ImageField(upload_to='profile_pics/')
    bio = md.TextField(max_length = 300)
    display_name = md.CharField(max_length = 100)
    profession = md.ManyToManyField(Profession)
    email=md.EmailField(max_length=255)
    created_on = md.DateField(auto_now_add = True)

    @receiver(post_save, sender = User)
    def create_profile(sender,instance,created ,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender = User)
    def save_profile(sender, instance,**kwargs):
        instance.profile.save()

    def __str__(self):
        return f'{self.user.username}'
