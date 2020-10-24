from django.urls import path
from .views import api_get_article_list,api_get_article_detail,api_post_article,api_update_article_detail,api_delete_article

app_name='article'

urlpatterns = [
    path('',api_get_article_list,name = "article_List"),
    path('<int:pk>/',api_get_article_detail,name = "article_detail"),
    path('create/',api_post_article,name="create_article"),
    path('<int:pk>/update/',api_update_article_detail,name="update_article"),
    path('<int:pk>/delete/',api_delete_article,name="delete_article")

    
]
