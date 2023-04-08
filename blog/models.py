from django.utils import timezone
from django.db import models
# Create your models here.
from django.db import models


class Post(models.Model):
    image = models.ImageField(upload_to='blog/static/posts/')
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    short_text = models.TextField()
    full_text = models.TextField()
    objects = models.Manager()


class Comment(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)
    objects = models.Manager()
