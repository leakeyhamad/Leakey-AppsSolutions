from django import views
from .views import signin, signout, signup, index, upload_project, comment
from django.urls import path

urlpatterns = [
    path('',views.index, name="index"),
    path('/register',views.signup, name="register"),
    path('/login',views.signin, name="login"),
    path('/project', views.upload_project, name="project"),
    path('/project', views.comment, name='project'),
]