from rest_framework import serializers
from .models import Member

class MemberGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id','clubMember','club']
        depth = 2

class MemberPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id','clubMember','club']
