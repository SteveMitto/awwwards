from django.db import models as md
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime
from decimal import Decimal
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
    design =md.DecimalField(max_digits=3, decimal_places=2 )
    usability =md.DecimalField(max_digits=3, decimal_places=2 )
    content =md.DecimalField(max_digits=3, decimal_places=2 )
    creativity = md.DecimalField(max_digits=3, decimal_places=2, null = True,blank=True)
    avarage = md.DecimalField(max_digits=3, decimal_places=2, null = True,blank=True)

    class Meta:
        ordering=['avarage']

    def __str__(self):
        return f"{self.user}s rating  "

    def save_rates(self):
        self.save()

    @property
    def int(self):
        for i in str(self.avarage):
            return i

    @property
    def dec(self):
        res=''
        for l in str(self.avarage):
            res+=l

        return res[1:]

@receiver(pre_save,sender=Rating)
def perform_calculations(sender ,instance, **kwargs):
    design = Decimal(instance.design)*Decimal(0.98)
    instance.design = design
    usability =  Decimal(instance.usability)*Decimal(0.98)
    instance.usability = usability
    content = Decimal(instance.content/10)*Decimal(9.8)
    instance.content = content
    if instance.creativity:
        creativity = Decimal(instance.creativity/10)*Decimal(9.8)
        instance.creativity = creativity
        avarage = (design+usability+content+creativity)/4
        instance.avarage= avarage
    else:
        avarage = (design+usability+content)/3
        instance.avarage= avarage

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

class Sotd(md.Model):
    post = md.ForeignKey(Post,on_delete=md.CASCADE, related_name='sotd')
    t_date = md.DateField(auto_now_add=True)


    @receiver(post_save, sender=Rating)
    def add_sotd(sender,created,instance,**kwargs):
        if created:
            if instance.post.posted_on.strftime("%Y-%m-%d") == datetime.today().strftime("%Y-%m-%d") :
                sotd = Sotd.objects.filter(t_date = instance.post.posted_on.strftime("%Y-%m-%d") ).first()
                if sotd != None:
                    insta=[]
                    instance_all =instance.post.ratings.all()
                    for post in instance_all:
                        insta.append(int(post.avarage))
                    instance_len=len(insta)
                    try:
                        instance_avarage =sum(insta)/instance_len
                    except:
                        instance_avarage =0

                    sotd_list=[]
                    sotd_count =sotd.post.ratings.all()
                    for post in sotd_count:
                        sotd_list.append(int(post.avarage))
                    sotd_len=len(sotd_list)
                    try:
                        sotd_avarage =sum(sotd_list)/sotd_len
                    except ZeroDivisionError:
                        sotd_avarage=0


                    if sotd_avarage > instance_avarage:
                        sotd.post = sotd.post

                    elif sotd_avarage == instance_avarage:
                        sotd.post = sotd.post

                    else:
                         sotd.post = instance.post

                else:
                    Sotd.objects.create(post=instance.post)

    @receiver(post_save, sender=Rating)
    def save_sotd(sender,instance,**kwargs):
        if instance:
            try:
                instance.sotd.save()
            except:
                pass
    def __str__(self):
        return f'{self.post} SOTD {self.t_date}'

    @property
    def final_results(self):
        design=[]
        usability=[]
        content=[]
        creativity=[]
        for rate in self.post.ratings.all():
            design.append(rate.design)
            usability.append(rate.usability)
            content.append(rate.content)
            creativity.append(rate.creativity)
        s_design={"value":str(sum(design)/len(design)),"color":"200,0,0","name":"design"}
        s_usability={"value":str(sum(usability)/len(usability)),"color":"0,200,200","name":"usability"}
        s_content={"value":str(sum(content)/len(content)),"color":"0,0,200","name":"content"}
        try:
            s_creativity={"value":str(sum(creativity)/len(creativity)),"color":"0,200,0","name":"creativity"}
        except:
            s_creativity={"value":0,"color":"0,200,0","name":"creativity"}
        sotd_res=[s_design,s_usability,s_content,s_creativity]
        return sotd_res
    @property
    def int(self,*args):
        for i in str(self.avarage):
            return i
