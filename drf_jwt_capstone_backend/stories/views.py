from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.apps import apps
from .models import Story
from .serializers import StoryGetSerializer
from .serializers import StoryPostSerializer

from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_stories(request):
    stories = Story.objects.all()
    serializer = StoryGetSerializer(stories, many=True)
    return Response(serializer.data)


@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def user_stories(request):
    if request.method == 'POST':
        serializer = StoryPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(storyAuthor=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        stories = Story.objects.filter(storyAuthor=request.user.id)
        serializer = StoryGetSerializer(stories, many=True)
        return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def stories_delete(request, pk):
    if request.method == "DELETE":
        stories = Story.objects.filter(id=pk)
        stories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_story(request, pk):
    if request.method == 'GET':
        story = Story.objects.get(id=pk)
        serializer = StoryGetSerializer(story)
        return Response(serializer.data, status=status.HTTP_200_OK)