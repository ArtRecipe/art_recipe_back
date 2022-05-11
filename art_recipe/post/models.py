from django.db import models
from accounts.models import User



class Post(models.Model):
    writer=models.ForeignKey(User, related_name="post", on_delete=models.CASCADE)
    title=models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bookmarkers=models.ManyToManyField(User, related_name="bookmarked_post", blank=True)
    color=models.CharField(max_length=256, blank=True)
    desc = models.TextField(blank=True)
    url = models.URLField(blank=True)

    @property
    def bookmarks(self):
        return self.bookmarkers.count()

    def bookmark(self, user):
        if user in self.bookmarkers.all():
            self.bookmarkers.remove(user)
        else:
            self.bookmarkers.add(user)
        self.save()

class PostImage(models.Model):
    post=models.ForeignKey(Post, related_name="images", on_delete=models.CASCADE)
    image=models.FileField(upload_to="files/")

class Material(models.Model):
    post=models.ForeignKey(Post, related_name="materials", on_delete=models.CASCADE)
    name=models.CharField(max_length=64)
    url=models.URLField(blank=True)