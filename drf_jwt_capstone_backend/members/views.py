from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.apps import apps

from .models import Member
from .serializers import MemberGetSerializer
from .serializers import MemberPostSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_members(request):
    members = Member.objects.all()
    serializer = MemberGetSerializer(members, many=True)
    return Response(serializer.data)


@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def user_members(request):
    if request.method == 'POST':
        serializer = MemberPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(clubMember=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        members = Member.objects.filter(clubMember=request.user)
        serializer = MemberGetSerializer(members, many=True)
        return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_Member(request, pk):
    if request.method == "DELETE":
        stories = Member.objects.filter(id=pk)
        stories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    
