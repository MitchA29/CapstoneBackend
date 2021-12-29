from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Club(models.Model):
    clubCreator = models.ForeignKey(User, on_delete=models.CASCADE)
    clubName = models.CharField(max_length=50)
    clubDescription = models.CharField(max_length=500)
    clubBook = models.CharField(max_length=500)
    






