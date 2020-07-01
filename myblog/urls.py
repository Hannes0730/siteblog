"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import HomeView, ArticleDetail, AddPost, UpdatePost, DeletePost, CategoryView, LikeView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetail.as_view(), name="article-detail"),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('article/edit-post/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('article/delete-post/<int:pk>', DeletePost.as_view(), name='delete_post'),
    path('category/<str:dogs>/', CategoryView, name='category'),
    path('like/post/<int:pk>/', LikeView, name='like_post'),
]
