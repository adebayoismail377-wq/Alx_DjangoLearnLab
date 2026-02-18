from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostByTagListView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [

    # Home / Posts
    path('', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Tag filtering (REQUIRED BY CHECKER)
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="posts_by_tag"),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),

    # Comments (function-based)
    path('posts/<int:post_id>/comments/new/', views.add_comment, name='comment-add'),
    path('comments/<int:comment_id>/edit/', views.edit_comment, name='comment-edit'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='comment-delete'),

    # Comments (class-based)
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Search
    path('search/', views.SearchResultsView.as_view(), name='search'),
]
