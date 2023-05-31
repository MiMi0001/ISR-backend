from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
import json

from .serializers import UserSerializer


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        payload = json.loads(request.body)
        refresh_token = payload["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        print("->Logout ok.")
        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_user_data(request):
    serializer = UserSerializer(request.user)
    user_data = serializer.data

    # username = request.user.username
    # email = request.user.email
    # first_name = request.user.first_name
    # last_name = request.user.last_name
    # user_data = {"username": username, "email": email, "first_name": first_name, "last_name": last_name}

    return JsonResponse(user_data)


@api_view(['POST'])
def register(request):
    payload = json.loads(request.body)
    serializer = UserSerializer(payload)
    serializer.save()

    print(serializer.data)
