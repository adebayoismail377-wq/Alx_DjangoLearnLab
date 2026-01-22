Create
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
Expected Output:
Book instance created successfully.
Retrieve
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
Expected Output:
('1984', 'George Orwell', 1949)
Update
book.title = "Nineteen Eighty-Four"
book.save()
Expected Output:
Title updated to 'Nineteen Eighty-Four'.
Delete
book.delete()
Book.objects.all()
Expected Output:
<QuerySet []>