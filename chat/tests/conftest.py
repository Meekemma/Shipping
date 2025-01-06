import pytest
from channels.testing import WebsocketCommunicator
from shipping.asgi import application
from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model
User = get_user_model()
from chat.models import  PrivateChatRoom
from rest_framework.test import APIClient




@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    def _create_user(email,password,first_name,last_name):
        user=User.objects.create_user(email=email,password=password,first_name=first_name,last_name=last_name)
        return user
    return _create_user


@pytest.fixture
def create_chat_room():
    def _create_chat_room(name, user1=None, user2=None, guest_user=None):
        chat_room = PrivateChatRoom.objects.create(name=name, user1=user1, user2=user2, guest_user=guest_user)
        return chat_room
    return _create_chat_room
