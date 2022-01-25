from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE
User = get_user_model()

class Story(models.Model):
    storyAuthor = models.ForeignKey(User, on_delete = models.CASCADE)
    storyDocument = models.TextField()
    storyName = models.CharField(max_length=100)
    storyDescription = models.CharField(max_length=500)
    storyGenre = models.CharField(max_length=100)
    
