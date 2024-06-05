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
        fields = ['id', 'first_name', 'last_name', 'image', 'user']

class MessageSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S UTC")
    likes_count = serializers.IntegerField(
        source='likes.count',
        read_only=True
    )

    class Meta:
        model = Message
        fields = ['id', 'author', 'created_at', 'content', 'image', 'likes_count']