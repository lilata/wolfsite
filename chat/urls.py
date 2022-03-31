from django.urls import path
from . import views
urlpatterns = [
    path('', views.chat, name='chat_index'),
    path('new_room/', views.new_room, name='chat_newroom'),
    path('room/<str:room_name>/', views.room, name='chat_room'),
]