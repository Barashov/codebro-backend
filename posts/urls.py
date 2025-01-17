from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.PostAPIView.as_view()),
    path('categories/', views.get_categories),
    path('category/<pk>/', views.PostCategoriesAPIView.as_view()),
    path('posts/', views.AllPostsAPIView.as_view()),
    path('post/<pk>/', views.post_view),
    path('following-posts/', views.FollowingPostsAPIView.as_view()),
    path('follow-post/<post_pk>/', views.FollowPost.as_view()),
]
