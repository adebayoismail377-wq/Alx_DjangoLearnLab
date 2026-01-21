from django.urls import path
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(template_name='relationship_app/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='relationship_app/logout.html'),
        name='logout'
    ),
    path('register/', views.register, name='register'),
]
 
 # website direction

urlpatterns = [
    # Role-based pages
    path('admin-page/', views.admin_view, name='admin_view'),
    path('librarian-page/', views.librarian_view, name='librarian_view'),
    path('member-page/', views.member_view, name='member_view'),

    # Authentication
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]

# Define url for book view
urlpatterns = [
    # List all books (optional, for reference)
    path('books/', views.book_list, name='book_list'),

    # Add a book
    path('books/add/', views.add_book, name='add_book'),

    # Edit a book
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),

    # Delete a book
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]
