from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from api.models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    Ensures CRUD operations behave correctly
    and return accurate status codes and data.
    """

    def setUp(self):
        """
        Runs before every test.
        Creates a test user, author, and book.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )
        self.client.login(username='testuser', password='password123')

        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )

        self.book_url = reverse('book-list')

    def test_create_book(self):
        """
        Test creating a new book via the API.
        """
        data = {
            "title": "New Book",
            "publication_year": 2019,
            "author": self.author.id
        }
        response = self.client.post(self.book_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_retrieve_books(self):
        """
        Test retrieving all books.
        """
        response = self.client.get(self.book_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_book(self):
        """
        Test updating a book's title.
        """
        url = reverse('book-detail', args=[self.book.id])
        data = {
            "title": "Updated Title",
            "publication_year": 2020,
            "author": self.author.id
        }

        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        """
        Test deleting a book.
        """
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
