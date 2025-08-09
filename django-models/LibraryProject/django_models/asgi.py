"""
ASGI config for LibraryProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import sys
import django

# Add the project root (one level up from this file) to PYTHONPATH
Project_Root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(Project_Root)

# Point to the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibaryProject.settings')

django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)


def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []


def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


if __name__ == "__main__":
    print("Books by Author 'John Doe':")
    for book in books_by_author("John Doe"):
        print("-", book)

    print("\nBooks in Library 'Central Library':")
    for book in books_in_library("Central Library"):
        print("-", book)

    print("\nLibrarian for 'Central Library':")
    librarian = librarian_for_library("Central Library")
    if librarian:
        print(librarian.name)
    else:
        print("No librarian found.")

