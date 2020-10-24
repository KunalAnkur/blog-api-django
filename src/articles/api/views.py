
from articles.models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view ,permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([AllowAny])
def api_get_article_list(request):
    try:
        article = Article.objects.all()
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    

    if request.method == 'GET':
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)    

@api_view(['GET'])
@permission_classes([AllowAny])
def api_get_article_detail(request,pk):
    try:
        article_detail = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        serializer = ArticleSerializer(article_detail)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST',])
@permission_classes([AllowAny])
def api_post_article(request):
    user= User.objects.get(id=request.user.id)
    article = Article()
    data = {
        'title':request.data['title'],
        'content':request.data['content'],
        'posted_by':user.id
    }
   
    if request.method == 'POST':
        serializer = ArticleSerializer(article,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT',])
@permission_classes([AllowAny])
def api_update_article_detail(request,pk):
    try:
        article_detail = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'PUT':
        serializer = ArticleSerializer(article_detail,data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    


@api_view(['DELETE',])
@permission_classes([AllowAny])
def api_delete_article(request,pk):
    try:
        article_detail = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'DELETE':
        operation = article_detail.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)   