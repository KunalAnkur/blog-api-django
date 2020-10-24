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
    return Response({'msg':'api is workin'})