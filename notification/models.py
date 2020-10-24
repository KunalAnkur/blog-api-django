from django.db import models
from django.conf import settings
# import uuid

class Notification(models.Model):
    id=models.IntegerField(primary_key=True)
    notification_type = models.CharField( max_length=50)
    article_title = models.CharField( max_length=50)
    article_author = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE,related_name='author')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    seen_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.article_title)

   