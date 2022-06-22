from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from model_utils import Choices  #used foe status fields

# Create your models here.
class Project(models.Model):
    SIZE=(
        ('simple', 'simple'),
        ('medium', 'medium'),
        ('complex', 'complex')
    )

    title=models.CharField(max_length=50)
    description=models.TextField(max_length=250)
    mvp=models.CharField(max_length=150)
    technologies=models.CharField(max_length=100)
    size=models.CharField(max_length=10, choices=SIZE)
    fullnames=models.CharField(max_length=30)
    contacts=models.CharField(max_length=13)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='project')

    def __str__(self):
        return self.title
    def save_project(self):
        self.save()
    def delete_project(self):
        self.delete()

class Status(models.Model):
    STATUSES=Choices('draft','published')
    status = models.IntegerField(choices=STATUSES, default=STATUSES.draft)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    project=models.OneToOneField(Project, on_delete=models.CASCADE)
    # pending=models.BooleanField(verbose_name=('pending'), default=False)
    # complete=models.BooleanField(verbose_name=('complete'), default=False) 

    def __str__(self):
        return self.status
    def save_status(self):
        self.save()
    def delete_status(self):
        self.delete()

class Comment(models.Model):
    comment=models.TextField(max_length=150)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['created_on']

    def __str__(self):
        return self.comment
    def save_comment(self):
        self.save()
    def delete_comment(self):
        self.delete()





