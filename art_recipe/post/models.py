from django.db import models
from accounts.models import User


class Material(models.Model):
    name=models.CharField(max_length=64)
    url=models.URLField(blank=True)

class Post(models.Model):
    writer=models.ForeignKey(User, related_name="post", on_delete=models.CASCADE)
    title=models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bookmarks=models.ManyToManyField(User, related_name="bookmarked_post", blank=True)
    thumbnail = models.FileField(upload_to="files/")
    material=models.ManyToManyField(Material, related_name="post", blank=True)
    color=models.CharField(max_length=256, blank=True)
    desc = models.TextField(blank=True)

class PostImage(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    image=models.FileField(upload_to="files/")