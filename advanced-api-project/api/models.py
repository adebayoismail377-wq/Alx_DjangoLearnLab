# Create your models here.

from django.db import models

class Author(models.Model):
    """
    Author model represents a writer who can have multiple books.
    This establishes a one-to-many relationship:
    one Author → many Book instances.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a published book.
    Each book is linked to exactly one Author via a foreign key.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()

    # ForeignKey creates a one-to-many relationship with Author
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

