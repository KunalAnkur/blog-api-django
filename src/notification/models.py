from django.db import models
from django.conf import settings
from articles.models import Article
from django.db.models.signals import post_save
# Create your models here.
class Notification(models.Model):
    notification_type = models.CharField( max_length=50)
    article_title = models.CharField( max_length=50)
    article_author = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE,related_name='author')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    seen_status = models.BooleanField(default=False)

    def __str__(self):
        return self.notification_type


def create_notification(sender, instance,created, **kwargs):
    data = {}
    data['notification_type']='article created'
    data['article_title']=instance.title
    data['article_author']=instance.posted_by
    
    if(created):
        print(instance.id)
        Notification.objects.create(notification_type='article created',article_title=instance.title,article_author=instance.posted_by)

post_save.connect(create_notification, sender=Article)        