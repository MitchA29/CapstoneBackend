from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.apps import apps

from .models import Favorite
from .serializers import FavoriteGetSerializer
from .serializers import FavoritePostSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_favorites(request):
    favorites = Favorite.objects.all()
    serializer = FavoriteGetSerializer(favorites, many=True)
    return Response(serializer.data)


@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def user_favorites(request):
    if request.method == 'POST':
        serializer = FavoritePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(favoriteOwner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        favorites = Favorite.objects.filter(favoriteOwner=request.user)
        serializer = FavoriteGetSerializer(favorites, many=True)
        return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_Favorite(request, pk):
    if request.method == "DELETE":
        stories = Favorite.objects.filter(id=pk)
        stories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    


