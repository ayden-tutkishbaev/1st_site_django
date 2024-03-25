from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    photo = models.ImageField(upload_to='articles/', null=True, blank=True)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return self.title


class Profile(models.Model):
    phone = models.CharField(max_length=255, default='')
    address = models.TextField(default='')
    job = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to='profiles', null=True, blank=True)
    description = models.CharField(max_length=300, default='Bio')
    # subscription = models.IntegerField(default=0)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.author.username