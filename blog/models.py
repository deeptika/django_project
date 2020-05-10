from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#0001_initial.py
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)  #auto_now = True, auto_now_add = True
    author = models.ForeignKey(User, on_delete = models.CASCADE)    #user deleted, posts deleted


