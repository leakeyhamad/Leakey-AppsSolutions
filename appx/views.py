from urllib import request
from django.shortcuts import render
from appx.models import Project, Status ,Comment
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.methodd=='POST':
         username=request.POST["username"]
         email=request.POST["email"]
         password1=request.POST["password1"]
         password2=request.POST["password2"]
         if password1!=password2:
             messages.error("incorrect password/ passwords do not match!")
             return redirect('/register')
         new_user=User.objects.create_user(
             username=username,
             email=email,
             password=password1,
         )
         new_user.save()
         redirect('/login')
    return render(request,'register.html')


def signin(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.sucess(request, "You have logged in successfully")
            redirect('/project')
    return render(request, 'login.html')        


def signout(request):
    logout(request)
    redirect(request, 'index.html') 