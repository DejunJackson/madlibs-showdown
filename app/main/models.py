from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True, null=False)
    username = models.CharField(max_length=128, unique=True, null=False)
    password = models.CharField(max_length=128, unique=False, null=False)
    first_name = models.CharField(max_length=128, unique=False, null=True, blank=True)
    last_name = models.CharField(max_length=128, unique=False, null=True, blank=True)
    score = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ["username"]



class Story(models.Model):
    title = models.CharField(max_length=128, unique=False, null=False)
    story_text = models.TextField(unique=True, null=False)
    questions = ArrayField(models.CharField(max_length=230))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]

class Game(models.Model):
    time = models.DateField(auto_now=False, auto_now_add=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    players = models.ManyToManyField(User)

    class Meta:
        ordering = ["time"]