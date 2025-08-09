from django.shortcuts import render
from .models import Book
from django.http import HttpResponse

from django.views.generic.detail import DetailView
from .models import Library


# Function-based view to list all books with author names
def list_books(request):
    books = Book.objects.all()
    # Render the books in the template
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship/library_detail.html'
    context_object_name = 'library'
