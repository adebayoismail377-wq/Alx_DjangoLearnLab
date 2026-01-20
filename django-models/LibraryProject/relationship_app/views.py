from django.shortcuts import render
# relationship_app/views.py

from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
# Create your views here.

from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # This makes {{ library }} available in the template

    # Note: In the template, you can access all books in the library with library.books.al