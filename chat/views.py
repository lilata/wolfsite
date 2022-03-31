from uuid import uuid4
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from . import models
# Create your views here.
@login_required
def chat(request):
    return render(request, 'chat/chat_index.html')

@login_required
def new_room(request):
    room_name = str(uuid4())
    return redirect(reverse('chat_room', kwargs={
        'room_name': room_name,
    }))


@login_required
def room(request, room_name):
    messages = models.ChatMessage.objects.filter(room_name=room_name).all()
    if not room_name.strip():
        return redirect(reverse('chat_index'))
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'messages': messages,
    })