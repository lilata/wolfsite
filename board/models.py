from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.
class BasicFields(models.Model):
    created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to='uploaded_images/', null=True, blank=True)


class Thread(BasicFields):
    def some_replies(self, count=2):
        r = Reply.objects.filter(
            belonging_thread=self
        ).all()[:count]
        return r

    def replies(self):
        r = Reply.objects.filter(belonging_thread=self).all()
        return r

    class Meta:
        verbose_name = 'Thread'
        verbose_name_plural = 'Threads'

class Reply(BasicFields):
    belonging_thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'