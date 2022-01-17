from rest_framework import serializers
from .models import Story

class StoryGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id','storyAuthor','storyDocument','storyName','storyDescription','storyGenre']
        depth = 1
class StoryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id','storyAuthor','storyDocument','storyName','storyDescription','storyGenre']
