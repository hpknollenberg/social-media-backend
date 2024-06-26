from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'profile_picture', 'user']


class MessageSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(many=False, read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S UTC")
    likes_count = serializers.IntegerField(
        source='likes.count',
        read_only=True
    )

    class Meta:
        model = Message
        fields = ['id', 'author', 'created_at', 'content', 'image', 'likes_count']



class CommentSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(many=False, read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S UTC")
    likes_count = serializers.IntegerField(
        source='likes.count',
        read_only=True
    )
    message = MessageSerializer(many=False, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'created_at', 'content', 'image', 'likes_count', 'message']


