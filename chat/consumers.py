from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import PrivateChatRoom, PrivateMessage
from django.contrib.auth import get_user_model
from datetime import datetime
from django.db import IntegrityError

User = get_user_model()
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json.get("message", "")
            guest_id = text_data_json.get("guest_id", None)
            target_user_id = text_data_json.get("target_user_id", None)

            if not message:
                raise ValueError("Invalid payload: 'message' is required.")

            # Authenticate sender
            if self.scope["user"].is_authenticated:
                sender = self.scope["user"]
                guest_sender = None
            else:
                sender = None
                guest_sender = guest_id

            if target_user_id:
                target_user = await User.objects.aget(id=target_user_id)
            else:
                target_user = None

            chat_room, created = await PrivateChatRoom.objects.aget_or_create(
                name=self.room_name,
                user1=sender,
                user2=target_user,
            )

            await PrivateMessage.objects.acreate(
                chat_room=chat_room,
                sender=sender,
                guest_sender=guest_sender,
                content=message
            )

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "message": message,
                    "sender": sender.username if sender else guest_sender or "Anonymous",
                    "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
            )
        except Exception as e:
            await self.send(text_data=json.dumps({"error": str(e)}))

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "type": "chat",
            "message": event["message"],
            "sender": event["sender"],
            "timestamp": event["timestamp"],
        }))
