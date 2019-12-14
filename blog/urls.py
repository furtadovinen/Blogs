from django.urls import path, include
from .views import (
    AllBlogsListView,
    AllBlogsDetailView,
    AllBlogsCreateView,
    AllBlogsUpdateView,
    AllBlogsDeleteView,
    UserAllBlogsListView
)
from . import views

urlpatterns = [
    path('', AllBlogsListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserAllBlogsListView.as_view(), name='user-blogs'),
    path('blog/<int:pk>/', AllBlogsDetailView.as_view(), name='detail'),
    path('blog/<int:pk>/update/', AllBlogsUpdateView.as_view(), name='update'),
    path('blog/<int:pk>/delete/', AllBlogsDeleteView.as_view(), name='delete'),
    path('blog/new/', AllBlogsCreateView.as_view(), name='create'),
    path('likes/<int:blog_id>/', views.likes, name='likes'),
    #path('', views.home, name='blog-home'),
]
