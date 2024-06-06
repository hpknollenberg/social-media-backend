from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status


from .models import *
from .serializers import *


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_comment(request):
  comment = Comment.objects.create(
    author = Profile.objects.get(id=request.data['profile']),
    content = request.data['content'],
    image = request.data['image'],
    message = Message.objects.get(id=request.data['message'])
  )
  comment_serialized = CommentSerializer(comment)
  if comment_serialized.is_valid():
    comment_serialized.save()
  return Response(comment_serialized.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_message(request):
  message = Message.objects.create(
    author = Profile.objects.get(id=request.data['profile']),
    content = request.data['message'],
    image = request.data['image']
  )
  message_serialized = MessageSerializer(message)
  if message_serialized.is_valid():
    message_serialized.save()
  return Response(message_serialized.data)


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


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment(request):
  comment = Comment.objects.get(id=request.data['id'])
  comment.delete()
  return Response()


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_message(request):
  message = Message.objects.get(id=request.data['id'])
  message.delete()
  return Response()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_comments(request):
  comments = Comment.objects.all().order_by('-created_at')
  comments_serialized = CommentSerializer(comments, many=True)
  return Response(comments_serialized.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_messages(request):
  messages = Message.objects.all().order_by('-created_at')
  messages_serialized = MessageSerializer(messages, many=True)
  return Response(messages_serialized.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_other_profile(request, pk):
  other_profile = Profile.objects.get(pk=pk)
  other_profile_serialized = ProfileSerializer(other_profile, many=False)
  return Response(other_profile_serialized.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_comment_likes(request):
    user = request.user
    profile = user.profile
    profile_likes = profile.likes_to_comment
    comment = Comment.objects.get(id=request.data['id'])
    if comment.likes.filter(id=profile.id).exists(): 
        profile_likes.remove(comment)
    else:
        profile_likes.add(comment)
    likes_serialized = CommentSerializer(profile_likes, many=True)
    return Response(likes_serialized.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_likes(request):
    user = request.user
    profile = user.profile
    profile_likes = profile.likes
    message = Message.objects.get(id=request.data['id'])
    if message.likes.filter(id=profile.id).exists(): 
        profile_likes.remove(message)
    else:
        profile_likes.add(message)
    likes_serialized = MessageSerializer(profile_likes, many=True)
    return Response(likes_serialized.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def update_profile_picture(request):
   user = request.user
   profile = user.profile
   profile.profile_picture = request.data['image']
   profile.save(update_fields=['profile_picture'])
   profile_update_serialized = ProfileSerializer(profile)
   return Response(profile_update_serialized.data)





