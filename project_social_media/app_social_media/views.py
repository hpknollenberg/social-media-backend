from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status


from .models import *
from .serializers import *



@api_view(['POST'])
@permission_classes([])
def create_user(request):
  user = User.objects.create(
    username = request.data['username'],
  )
  user.set_password(request.data['password'])
  user.save()
  profile = Profile.objects.create(
    user = user,
    first_name = request.data['first_name'],
    last_name = request.data['last_name']
  )
  profile.save()
  profile_serialized = ProfileSerializer(profile)
  return Response(profile_serialized.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_message(request):
  message = Message.objects.create(
    author = Profile.objects.get(id=request.data['profile']),
    content = request.data['message']
  )
  message_serialized = MessageSerializer(message)
  if message_serialized.is_valid():
    message_serialized.save()
    return Response(message_serialized.data, status=status.HTTP_201_CREATED)
  return Response(message_serialized.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_image(request):
  image_serialized = ImageSerializer(data=request.data)
  if image_serialized.is_valid():
    image_serialized.save()
    return Response(image_serialized.data, status=status.HTTP_201_CREATED)
  return Response(image_serialized.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_images(request):
  images = Image.objects.all()
  images_serialized = ImageSerializer(images, many=True)
  return Response(images_serialized.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_messages(request):
  messages = Message.objects.all().order_by('-created_at')
  messages_serialized = MessageSerializer(messages, many=True)
  return Response(messages_serialized.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_message(request):
  message = Message.objects.get(id=request.data['id'])
  message.delete()
