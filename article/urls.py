from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='blog-home'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('search/', views.searchposts, name='searchposts'),
]
