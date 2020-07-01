from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="Story Time!")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='random')
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    post_time = models.TimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    summary = models.CharField(max_length=255, default='Click the link to read the content!')
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    add_file = models.FileField(null=True, blank=True, upload_to="")

    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

