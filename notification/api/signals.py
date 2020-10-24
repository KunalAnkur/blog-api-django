from articles.models import Article
from django.db.models.signals import post_save
from django.dispatch import receiver
from notification.models import Notification

@receiver(post_save, sender=Article)
def create_notification(sender, instance,created, **kwargs):
    
    if(created):
        Notification.objects.create(notification_type='article created',article_title=instance.title,article_author=instance.posted_by)

# post_save.connect(create_notification, sender=Article)      