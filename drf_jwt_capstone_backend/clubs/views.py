from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Club
from .serializers import ClubGetSerializer
from .serializers import ClubPostSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_clubs(request):
    clubs = Club.objects.all()
    serializer = ClubGetSerializer(clubs, many=True)
    return Response(serializer.data)


@api_view(['POST','GET','DELETE'])
@permission_classes([IsAuthenticated])
def user_clubs(request):
    if request.method == 'POST':
        serializer = ClubPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(clubCreator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        clubs = Club.objects.filter(clubCreator=request.user.id)
        serializer = ClubGetSerializer(clubs, many=True)
        return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def clubs_delete(request, pk):
    if request.method == "DELETE":
        stories = Club.objects.filter(id=pk)
        stories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

