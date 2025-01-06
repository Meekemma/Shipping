from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()


class PrivateChatRoomSerializer(serializers.ModelSerializer):
    user1 = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    user2 = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = PrivateChatRoom
        fields = ['user1','user2', 'created_at']

class PrivateMessageSerializer(serializers.ModelSerializer):
    chat_room = serializers.PrimaryKeyRelatedField(queryset=PrivateChatRoom.objects.all())
    guest_sender = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = PrivateMessage
        fields = ['chat_room', 'sender', 'guest_sender', 'content', 'timestamp']
        read_only_fields = ['timestamp']