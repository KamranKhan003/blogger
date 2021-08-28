from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()


# Post Form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('slug','user')
        labels = {
            'contant': ' '
        }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control',"autocomplete":'off'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
        }


# Setting Form
class SettingForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','image')
        labels = {
            'email':'Email'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}),
            'last_name': forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}),
            'username': forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}),
            'email': forms.EmailInput(attrs={"class":"form-control","autocomplete":"off"}),
            'image': forms.FileInput(attrs={"class":"form-control"}),
        }


# Contact Form
class ContactForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',"autocomplete":"off",'placeholder':'Subject'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',"autocomplete":"off",'placeholder':'Email Adsress'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',"autocomplete":"off",'placeholder':'Message'}))


# Comment Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
        labels = {
            'comment': ' '
        }
        widgets = {
            'comment': forms.TextInput(attrs={'class':'form-control','placeholder':'Write Comment','autocomplete':'off'})
        }
