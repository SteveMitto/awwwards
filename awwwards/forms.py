from django import forms
from .models import Post,Image,Rating,Profile


class PostForm(forms.ModelForm):
    title=forms.CharField(max_length=200,label="Project name")
    description=forms.CharField(max_length=500,label="image description")
    main_image=forms.ImageField(label='Display Image')

    class Meta:
        model =Post
        fields=('title','description','main_image')
        widgets={
        'tags':forms.CheckboxSelectMultiple()
        }

class ImageForm(forms.ModelForm):
    image=forms.ImageField(label="Image")

    class Meta:
        model=Image
        fields=('image',)

class RatingForm(forms.ModelForm):
    design =forms.DecimalField(max_digits=3, decimal_places=2)
    usability =forms.DecimalField(max_digits=3, decimal_places=2)
    content =forms.DecimalField(max_digits=3, decimal_places=2)
    creativity =forms.DecimalField(max_digits=3, decimal_places=2)
    class Meta:
        model=Rating
        fields=('design','usability','content','creativity')

class ProfileForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=('profile_pic','country','profession','bio','display_name','link')
