from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(r'ws/chat/room/<room_name>/', consumers.ChatConsumer.as_asgi(),
         name='ws_chat_room'),
]
