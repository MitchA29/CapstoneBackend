from django.contrib.auth import get_user_model
from .serializers import RegistrationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
User = get_user_model()

from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes






class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


# @api_view(['POST','GET','DELETE'])
# @permission_classes([IsAuthenticated])
# def user_clubs(request):
#     if request.method == 'POST':
#         serializer = ClubSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(clubCreator=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'GET':
#         clubs = Club.objects.filter(clubCreator_id=request.user.id)
#         serializer = ClubSerializer(clubs, many=True)
#         return Response(serializer.data)
