from ckeditor.fields import RichTextField
from django.db import models
from user.models import User
from datetime import datetime


class Blog(models.Model):
    author = models.TextField(
        max_length=100, blank=True, null=True, default="unknown user", editable=False
    )
    title = models.CharField(
        max_length=100,
        unique=False,
    )
    desc = models.TextField(max_length=200, blank=False)
    blog_content = RichTextField(blank=True, null=True)
    thumbnail = models.URLField(max_length=400)
    read_more = models.URLField(max_length=400, blank=True)
    category = models.CharField(max_length=10, blank=True)
    id = models.AutoField(primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    approve_status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.user.username + " Comment: " + self.content
        
