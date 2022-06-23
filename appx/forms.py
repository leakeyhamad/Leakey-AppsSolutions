from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project, Comment


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude= ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 15, 'rows': 6}),
        } 



