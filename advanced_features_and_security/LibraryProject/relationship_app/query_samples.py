from relationship_app.models import Author, Book, Library, Librarian

import django
import os

# Setup Django environment so we can use ORM
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()




# 1. Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return []


# 2. List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []


# 3. Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian  # Access via reverse OneToOne relationship
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


if __name__ == "__main__":
    # Example calls:
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
