from django.shortcuts import render
from .models import Book
from django.http import HttpResponse

from django.views.generic.detail import DetailView
from .models import Library

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy


# Function-based view to list all books with author names
def list_books(request):
    books = Book.objects.all()
    # Render the books in the template
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# Login view using built-in Django LoginView
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout view using built-in Django LogoutView
class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('list_books')  # Redirect to some page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})