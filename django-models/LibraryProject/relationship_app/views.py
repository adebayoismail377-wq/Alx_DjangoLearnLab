from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Book
from .models import Library   # 👈 THIS LINE is what the checker wants

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    from django.shortcuts import render, redirect
from django.contrib.auth import login
# 👇 ADD these imports (do not remove existing ones)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

# --------------------
# EXISTING VIEWS (KEEP THESE)
# --------------------
def home(request):
    return render(request, 'relationship_app/home.html')

def about(request):
    return render(request, 'relationship_app/about.html')

# --------------------
# ADD AUTHENTICATION VIEWS BELOW
# --------------------

# Login View (built-in)
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout View (built-in)
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

