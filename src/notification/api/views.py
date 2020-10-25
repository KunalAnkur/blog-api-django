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
    page = int(request.GET.get('page'))
    limit = int(request.GET.get('limit'))
    startIndex = (page-1)*limit
    endIndex = page*limit
    try:
        notifications = Notification.objects.all()
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = NotificationSerializer(notifications, many=True)
        data = {}
        if endIndex < len(serializer.data):    
            data['next']={
                'page':page+1,
                'limit':limit
            }
        if startIndex>0:
            data['previous']={
                'page':page-1,
                'limit':limit
            }
        data['results'] = serializer.data[startIndex:endIndex]       
        return Response(data,status=status.HTTP_200_OK)


@api_view(['GET',])
@permission_classes([AllowAny])
def api_get_notification_for_user(request):
    page = int(request.GET.get('page'))
    limit = int(request.GET.get('limit'))
    startIndex = (page-1)*limit
    endIndex = page*limit
    try:
        user_notification = Notification.objects.exclude(article_author=request.user.id)
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = NotificationSerializer(user_notification, many=True) 
        data = {}
        if endIndex < len(serializer.data):    
            data['next']={
                'page':page+1,
                'limit':limit
            }
        if startIndex>0:
            data['previous']={
                'page':page-1,
                'limit':limit
            }
        data['results'] = serializer.data[startIndex:endIndex]      
        return Response(data,status=status.HTTP_200_OK)


@api_view(['PUT',])
@permission_classes([AllowAny])
def api_mark_notification_read(request):
    for id in request.data:
        try:
            notification =  Notification.objects.get(id=id)
            old_notification = notification
            notification.seen_status = True
            notification.save()
        except Notification.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
    
    return Response({"msg":"mark notification read"},status=status.HTTP_201_CREATED)    


    