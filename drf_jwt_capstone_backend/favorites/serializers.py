from rest_framework import serializers
from .models import Favorite

class FavoriteGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id','favoriteOwner','favoriteStory']
        depth = 2

class FavoritePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id','favoriteOwner','favoriteStory']
