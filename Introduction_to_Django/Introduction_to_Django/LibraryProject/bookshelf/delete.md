from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()
Expected Output:
<QuerySet []>
This confirms the book has been successfully deleted.