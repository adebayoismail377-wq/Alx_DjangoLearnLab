from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New ViewSet for full CRUD
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

"""
This ViewSet uses TokenAuthentication.
Only authenticated users can access this endpoint.
Authentication is handled via DRF's TokenAuthentication system.
"""


# Create your views here.
