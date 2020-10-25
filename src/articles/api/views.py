
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
    # print(request.GET.get('page'))
    # print(request.GET.get('limit'))
    page = int(request.GET.get('page'))
    limit = int(request.GET.get('limit'))
    startIndex = (page-1)*limit
    endIndex = page*limit

    try:
        article = Article.objects.all()
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    

    if request.method == 'GET':
        serializer = ArticleSerializer(article, many=True)
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
        # results = serializer.data[startIndex:endIndex]
        
        return Response(data,status=status.HTTP_200_OK)    

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
    user = request.user
    try:
        article_detail = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'DELETE':
        data = {}
        if article_detail.posted_by == user.id:
            operation = article_detail.delete()
            
            if operation:
                data["success"] = "delete successful"
                return Response(data=data,status=status.HTTP_200_OK)     
            else:
                data["failure"] = "delete failed"
                return Response(data=data,status=status.HTTP_400_BAD_REQUEST)   
        else:
            data["failure"] = "your not the author of this post"
            return Response(data=data,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET',])
@permission_classes([AllowAny])
def api_get_my_article_list(request):
    user = request.user
    page = int(request.GET.get('page'))
    limit = int(request.GET.get('limit'))
    startIndex = (page-1)*limit
    endIndex = page*limit
    try:
        articles = Article.objects.filter(posted_by=user.id)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(articles,many=True)
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
def api_get_my_article_detail(request,pk):
    user= request.user
    try:
        my_article_detail = Article.objects.get(id=pk,posted_by=user.id)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArticleSerializer(my_article_detail)  
        return Response(serializer.data,status=status.HTTP_200_OK)             
     
