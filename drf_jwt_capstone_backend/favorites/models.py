from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE
User = get_user_model()

class Favorite(models.Model):
    favoriteOwner = models.ForeignKey(User, on_delete = models.CASCADE)
    favoriteStory = models.ForeignKey('stories.Story', on_delete = models.CASCADE)
    
    
