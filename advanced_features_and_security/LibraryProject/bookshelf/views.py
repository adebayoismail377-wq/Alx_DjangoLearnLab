from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm

def book_list(request):
    books = Book.objects.all()

    if request.method == "GET":
        form = BookSearchForm(request.GET)
        if form.is_valid():
            title = form.cleaned_data['title']
            books = books.filter(title__icontains=title)
    else:
        form = BookSearchForm()

    return render(request, "bookshelf/book_list.html", {
        "books": books,
        "form": form
    })

# Create your views here.
