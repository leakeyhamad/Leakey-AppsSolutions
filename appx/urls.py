from django import views
from appx.views import signin, signout, signup, index
from django.urls import path

urlpatterns = [
    path('',views.index, name="index"),
    path('/register',views.signup, name="register"),
    path('/login',views.signin, name="login"),
]