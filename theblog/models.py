from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255,default='MY POST')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)
    post_time = models.DateTimeField(auto_now_add=True)

    category = models.CharField(max_length=255,default='coding')

    body = models.TextField()
    
    def __str__(self):
        return f"self.title | self.author"

    def get_absolute_url(self):
        return reverse("home", )
    
class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home", )