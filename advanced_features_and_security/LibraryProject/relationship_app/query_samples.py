import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return []


# Query 2: List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []


# Query 3: Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return Librarian.objects.get(library=library)  # ✅ explicit check
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


if __name__ == "__main__":
    print("Books by Author J.K. Rowling:")
    for book in books_by_author("J.K. Rowling"):
        print(f"- {book.title}")

    print("\nBooks in City Library:")
    for book in books_in_library("City Library"):
        print(f"- {book.title}")

    print("\nLibrarian of City Library:")
    librarian = librarian_for_library("City Library")
    print(librarian.name if librarian else "No librarian assigned")
