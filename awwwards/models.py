from django.db import models as md
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

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
    flags = md.URLField(null=True)
    class Meta:
        verbose_name='countries'
        ordering=['name']

    def __str__(self):
        return self.name
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

def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)

class Image(md.Model):
    post=md.ForeignKey(Post,on_delete=md.PROTECT,related_name="images")
    image= md.ImageField(upload_to=get_image_filename,verbose_name="Image")

    class Meta:
        verbose_name='image'

    def __str__(self):
        return f'{self.post} {len(self.image)} images'

    def save_post_image(self):
        self.save()

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

    def __str__(self):
        return f'{self.follower} follows {self.followed}'

class Like(md.Model):
    user = md.ForeignKey(User,on_delete=md.PROTECT , related_name ='liked_posts')
    post = md.ForeignKey(Post,on_delete=md.CASCADE, related_name='likes')

    class Meta:
        verbose_name='likes'

    def __str__(self):
        return f'{self.user} likes {self.post}'

# class Sotd(md.Model):
#     post = md.ForeignKey(Post,on_delete=md.CASCADE, related_name='sotd')
#     date = md.DateTimeField(auto_now_add=True)
#
#     @receiver(post_save, sender=Like)
#     def add_sotd(sender,created,instance,**kwargs):
#         if created:
#             posts = Post.objects.filter(posted_on__date = instance.posted_on ).all()
#             if posts:
#                 for post in posts:
#                     pass
#             else:
#                 SiteOfTheDay.objects.create(post)
#     @receiver(post_save, sender=Post)
#     def save_sotd(sender,intance,**kwargs):
#         instance.sotd.save()
