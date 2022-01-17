from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Story
from .serializers import StorySerializer
from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_stories(request):
    stories = Story.objects.all()
    serializer = StorySerializer(stories, many=True)
    return Response(serializer.data)


@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def user_stories(request):
    if request.method == 'POST':
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(storyAuthor_id=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        stories = Story.objects.filter(storyAuthor_id=request.user.id)
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)
    elif request.method == "DELETE":
        stories = Story.objects.filter(id = request.id)
        stories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
