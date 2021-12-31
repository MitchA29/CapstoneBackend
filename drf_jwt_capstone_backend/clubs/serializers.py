from rest_framework import serializers
from .models import Club

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id','clubCreator_id','clubName','clubDescription','clubBook']