from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    message = models.TextField()
    room_name = models.TextField()

    def message_text(self):
        return f'{self.user.username}({self.date.strftime("%b %d %Y %H:%M:%S")}): ' \
               f'{self.message}'