from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
       author = models.ForeignKey(User, on_delete=models.CASCADE)
       title = models.CharField(max_length=100)
       description = models.TextField()
       # For image or video, consider using models.ImageField or models.FileField with proper media settings

class Analytics(models.Model):
       post = models.OneToOneField(Post, on_delete=models.CASCADE)
       likes = models.IntegerField(default=0)
       shares = models.IntegerField(default=0)
       comments = models.IntegerField(default=0)

