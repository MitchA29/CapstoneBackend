from rest_framework import serializers
from .models import Club

class ClubGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id','clubCreator','clubName','clubDescription','clubBook']
        depth = 2

class ClubPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id','clubCreator','clubName','clubDescription','clubBook']