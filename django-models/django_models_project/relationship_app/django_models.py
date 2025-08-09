from django.db import models

# Author → can write many Books
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book → belongs to one Author, but an Author can have many Books
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  
    # CASCADE = if author is deleted, their books are deleted too

    def __str__(self):
        return f"{self.title} by {self.author.name}"


# Library → can have many Books, and Books can be in many Libraries
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)  

    def __str__(self):
        return self.name


# Librarian → exactly one Library has exactly one Librarian (One-to-One)
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.library.name}"
