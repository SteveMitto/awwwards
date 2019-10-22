from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse,HttpResponseRedirect
from .models import Country,Image,Profile,Post,Sotd,Rating
from .forms import PostForm,ImageForm,RatingForm
from django.forms import modelformset_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
def index(request):
    form = UserCreationForm()
    today = datetime.today().strftime("%Y-%m-%d")
    sotd = Sotd.objects.filter(t_date = today).first()
    if sotd == None:
        sotd = Sotd.objects.first()
    print("******************",sotd)
    context={
    'form':form,
    'sotd':sotd
    }
    return render(request,'index.html',context)

def signup(request):
    if request.method == "POST":
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    context={
    'form':form
    }
    return render(request,'registration/signup.html',context)

@login_required
def uploads(request):

    ImageFormSet = modelformset_factory(Image,form=ImageForm, extra=3)
    if request.method == "POST":
        post_form = PostForm(request.POST,request.FILES)
        image_form = ImageFormSet(request.POST,request.FILES,queryset=Image.objects.none())

        if post_form.is_valid() and image_form.is_valid():
            post_form.save(commit=False)
            post_form.user = request.user
            post_form.instance.user = request.user
            post_form.save()
            post=Post.objects.filter(title=post_form.cleaned_data['title']).first()
            for form in image_form.cleaned_data:
                if form:
                    image=form['image']
                    photo = Image(post=post, image=image)
                    photo.save()
            messages.success(request,"Awesome lets see it at home")
            return HttpResponseRedirect('/')
        else:
            print(post_form.errors, image_form.errors)

    else:

        post_form=PostForm()
        image_form=ImageFormSet(queryset=Image.objects.none())

    context = {
    'post_form':post_form,
    'image_form':image_form,
    }
    return render(request,'uploads.html',context)

@login_required
def search(request):
    if request.method == "GET":
        search_term=request.GET.get('search_term')
        users = User.objects.filter(username__icontains = search_term)
        websites = Post.objects.filter(title__icontains= search_term ,description__icontains= search_term )

        context={
        'users':users,
        'websites':websites
        }
        return render(request,'search.html',context)
    else:
        return HttpResponseRedirect('/')

@login_required
def site(request,id):
    website = Post.objects.get(pk = id)
    ratings_a =Rating.objects.filter(post=website).first()
    if request.method == "POST":
        form =RatingForm(request.POST)
        if form.is_valid():
            design =form.cleaned_data['design']
            usability =form.cleaned_data['usability']
            content =form.cleaned_data['content']
            creativity =form.cleaned_data['creativity']
            print('******************',design,'*',usability,'*',content,'*',creativity)
            ratings = Rating(user = request.user,post = website,design=design,usability=usability,content=content,creativity=creativity)
            ratings.save()
            return redirect(site,id)
    else:
        form =RatingForm()

    rate = Rating.objects.filter(user=request.user,post=website).first()
    rated = None
    if rate == None:
        rated = False
    else:
        rated = True

    context={
    'website':website,
    'form':form,
    'rated':rated,
    'ratings_a':ratings_a
    }
    return render(request,'site.html',context)

def profile(request,username):
    view_user = User.objects.filter(username = username).first()

    context={
    'view_user':view_user
    }
    return render(request,'profile.html',context)
