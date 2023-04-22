from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    logo = models.ImageField(null=True,blank=True,upload_to="images/")
class Board(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    board = models.ForeignKey(Board,related_name='topics',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic,related_name='posts',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
class recherche(models.Model):
    input = models.TextField(max_length=4000)
class Question(models.Model):
    text = models.TextField()
    choice1 = models.CharField(max_length=255)
    choice2 = models.CharField(max_length=255)
    choice3 = models.CharField(max_length=255)
    choice4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
class Video(models.Model):
    caption = models.CharField(max_length=80)
    video = models.FileField(upload_to="video/%y")
    minature = models.ImageField(null=True,blank=True,upload_to="images/")
    questions = models.ManyToManyField(Question)
    def __str__(self):
        return self.caption
