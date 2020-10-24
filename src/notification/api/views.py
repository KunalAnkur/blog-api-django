from notification.models import Notification
from .serializers import NotificationSerializer
from rest_framework.decorators import api_view ,permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# from django.contrib.auth.models import User

@api_view(['GET',])
@permission_classes([AllowAny])
def api_get_notifications(request):
    try:
        notifications = Notification.objects.all()
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = NotificationSerializer(notifications, many=True)       
        return Response(serializer.data,status=status.HTTP_200_OK)