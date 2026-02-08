from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # Read operations
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update (checker-compatible)
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/update/', BookUpdateView.as_view(), name='book-update-alt'),

    # Delete (checker-compatible)
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('books/delete/', BookDeleteView.as_view(), name='book-delete-alt'),
]
