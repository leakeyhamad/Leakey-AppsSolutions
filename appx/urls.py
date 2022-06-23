from django import views
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home, name="index"),
    path('register/',views.signup, name="register"),
    path('login/',views.signin, name="login"),
    path('upload/', views.upload_project, name="upload_project"),
    path('comment/', views.comment, name='comment'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)