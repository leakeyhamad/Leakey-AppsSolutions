from urllib import request
from django.shortcuts import render
from appx.models import Project, Status ,Comment
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'index.html')


def signup(request):
    if request.method=='POST':
         username=request.POST["username"]
         email=request.POST["email"]
         password1=request.POST["password1"]
         password2=request.POST["password2"]
         if password1!=password2:
             messages.error(request, "incorrect password/ passwords do not match!")
             return redirect('register')
         new_user=User.objects.create_user(
             username=username,
             email=email,
             password=password1,
         )
         new_user.save()
         return redirect('login')
    return render(request,'register.html')


def signin(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.sucess(request, "You have logged in successfully")
            return redirect('project')
    return render(request, 'login.html')  


def signout(request):
    logout(request)
    redirect(request, 'index.html') 


def comment(request):
    if request.method=='POST':
        form=CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.user=request.user
            comment.save()
            return redirect('index')
    else:
        form=CommentForm()
    return render(request, 'comment.html',{'form':form})  


@login_required
def upload_project(request):
    if request.method=='POST':
        form=ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.user=request.user
            project.save()
            messages.success("We have successfully received the projects details")
            return redirect('index')
    else:
        form=ProjectForm()        
    return render(request, 'project.html', {'form':form}) 


          

