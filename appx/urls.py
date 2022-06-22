from django import views
from appx.views import signin, signout, signup, index, upload_project
from django.urls import path

urlpatterns = [
    path('',views.index, name="index"),
    path('/register',views.signup, name="register"),
    path('/login',views.signin, name="login"),
    path('/project', views.upload_project, name="project"),
]