from django.urls import path
from . import views

urlpatterns = [
    # Function-based view: list all books
    path('books/', views.list_books, name='list_books'),

    # Class-based view: show details of a specific library
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
