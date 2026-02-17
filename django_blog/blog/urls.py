from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

urlpatterns = [
    path('register/', views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(
        template_name='blog/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        template_name='blog/logout.html'), name='logout'),

    path('profile/', views.profile, name='profile'),
]

from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),                   # List all posts
    path('post/new/', PostCreateView.as_view(), name='post-create'),       # Create new post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Edit post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete post
]


urlpatterns += [
    path('posts/<int:post_id>/comments/new/', views.add_comment, name='comment-add'),
    path('comments/<int:comment_id>/edit/', views.edit_comment, name='comment-edit'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='comment-delete'),
]

from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns += [
    path(
        'posts/<int:post_id>/comments/new/',
        CommentCreateView.as_view(),
        name='comment-create'
    ),
    path(
        'posts/<int:post_id>/comments/<int:pk>/update/',
        CommentUpdateView.as_view(),
        name='comment-update'
    ),
    path(
        'posts/<int:post_id>/comments/<int:pk>/delete/',
        CommentDeleteView.as_view(),
        name='comment-delete'
    ),
]
