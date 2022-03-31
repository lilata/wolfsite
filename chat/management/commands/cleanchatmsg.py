import datetime

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone
from chat.models import ChatMessage

class Command(BaseCommand):
    help = 'Delete old messages'
    def handle(self, *args, **options):
        days = settings.KEEP_CHAT_MESSAGE_DAYS
        now = timezone.now()
        d = now - datetime.timedelta(days=days)
        to_delete = ChatMessage.objects.filter(date__lte=d).all()
        to_delete_pks = ' '.join([str(x.pk) for x in to_delete])
        if to_delete_pks.strip():
            print('Deleting', to_delete_pks)
        to_delete.delete()

