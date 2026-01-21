from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
Expected Output:
A Book object is successfully created and saved to the database.
The variable book now holds the created Book instance.