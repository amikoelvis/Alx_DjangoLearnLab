# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
import os
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    published_date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()  # new field

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

def user_avatar_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/avatars/user_<id>/<filename>
    return f'avatars/user_{instance.user.id}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to=user_avatar_path, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

# Signal: create/update Profile automatically
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        # ensure a profile exists
        Profile.objects.get_or_create(user=instance)
