import json
from django.contrib.auth.models import User
from django.utils import timezone
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from . import models

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope['user'].is_authenticated is False:
            await self.close()
        else:
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = 'chat_%s' % self.room_name

            # Join room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        if not message.strip():
            return
        username = self.scope['user'].username
        date_now = timezone.now()
        message_json = {
            'message': message,
            'username': username,
            'date': date_now.strftime("%b %d %Y %H:%M:%S")
        }
        user = await database_sync_to_async(User.objects.get)(username=username)
        cm = models.ChatMessage(user=user, date=date_now,
                                message=message, room_name=self.room_name)
        await database_sync_to_async(cm.save)()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message_json
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message['message'],
            'username': message['username'],
            'date': message['date']
        }))