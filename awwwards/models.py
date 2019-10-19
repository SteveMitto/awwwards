from django.db import models as md
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profession(md.Model):
    profession = md.CharField(max_length=100)

    class Meta:
        ordering=['profession']
        verbose_name = 'profession'

    def __str__(self):
        return f'{self.profession}'

    def save_professions(self):
        self.save()

class Country(md.Model):
    name = md.CharField(max_length=100)

    class Meta:
        verbose_name='countries'
        ordering=['name']

    def save_country(self):
        self.save()

class Profile(md.Model):
    user = md.OneToOneField(User,on_delete=md.PROTECT)
    profile_pic= md.ImageField(upload_to='profile_pics/',default="profile_pics/default.png")
    country=md.ForeignKey(Country,on_delete=md.CASCADE , related_name = 'profile',null=True)
    bio = md.TextField(max_length = 300, blank=True)
    display_name = md.CharField(max_length = 100,blank=True)
    profession = md.ManyToManyField(Profession,blank=True)
    created_on = md.DateField(auto_now_add = True,blank=True)

    class Meta:
        verbose_name='profile'
    @receiver(post_save, sender = User)
    def create_profile(sender,instance,created ,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender = User)
    def save_profile(sender, instance,**kwargs):
        instance.profile.save()


    def __str__(self):
        return f'{self.user.username}'

class Tag(md.Model):
    tags= md.CharField(max_length=100)

    class Meta:
        verbose_name='tags'

    def __str__(self):
        return f'{self.tags}'

class Post(md.Model):
    user = md.ForeignKey(User,on_delete=md.PROTECT,related_name='posts')
    title= md.TextField(max_length=300)
    description = md.TextField(max_length=500)
    tags = md.ManyToManyField(Tag)
    main_image =md.ImageField(upload_to='main_image/')
    posted_on=md.DateField(auto_now_add = True)

    class Meta:
        verbose_name='posts'

    def __str__(self):
        return f'{self.title}'

class Contributor(md.Model):
    post=md.ForeignKey(Post,on_delete=md.PROTECT,related_name="contributors")
    contributors=md.ManyToManyField(User)

    class Meta:
        ordering=['post']

    def __str__(self):
        return f"{self.post}"

    def save_contribs(self):
        self.save()

class Rating(md.Model):
    post=md.ForeignKey(Post,on_delete=md.PROTECT,related_name="ratings")
    user=md.ForeignKey(User,on_delete=md.PROTECT,related_name="my_ratings")
    design =md.IntegerField()
    usability =md.IntegerField()
    content =md.IntegerField()
    creativity = md.IntegerField(blank = True)
    avarage = md.IntegerField()

    class Meta:
        ordering=['avarage']

    def __str__(self):
        return f"{self.user}s rating  "

    def save_rates(self):
        self.save()

class Follow(md.Model):
    follower=md.ForeignKey(User,on_delete=md.CASCADE,related_name='following')
    followed =md.ForeignKey(User,on_delete=md.CASCADE,related_name='followers')

    class Meta:
        ordering=['followed']

    def save_follow(self):
        self.save()

class Like(md.Model):
    user = md.ForeignKey(User,on_delete=md.PROTECT , related_name ='liked_posts')
    post = md.ForeignKey(Post,on_delete=md.CASCADE, related_name='likes')

    class Meta:
        verbose_name='likes'
