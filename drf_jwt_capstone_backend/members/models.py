from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE
User = get_user_model()

class Member(models.Model):
    clubMember = models.ForeignKey(User, on_delete = models.CASCADE)
    club = models.ForeignKey('clubs.Club', on_delete = models.CASCADE)
    
    