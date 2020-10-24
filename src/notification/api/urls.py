from django.urls import path
from .views import api_get_notifications
app_name='notification'

urlpatterns = [
    path('get-notification',api_get_notifications,name="notification_list")
]
