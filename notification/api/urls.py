from django.urls import path
from .views import api_get_notifications,api_get_notification_for_user,api_mark_notification_read
app_name='notification'

urlpatterns = [
    path('get-notification/',api_get_notifications,name="notification_list"),
    path('get-user-notification/',api_get_notification_for_user,name="notification_list_for_user"),
    path('mark-notification-read/',api_mark_notification_read,name="mark_notification_read")
]
