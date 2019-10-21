from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse,HttpResponseRedirect
from .models import Country,Image,Profile,Post
from .forms import PostForm,ImageForm # Create your views here.
from django.forms import modelformset_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def index(request):
    form = UserCreationForm()
    return render(request,'index.html',{'form':form})

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
