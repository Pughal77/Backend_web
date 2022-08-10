from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class community_article_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="identification")
    title = models.CharField(max_length=20)
    entry = models.CharField(max_length=200)




    