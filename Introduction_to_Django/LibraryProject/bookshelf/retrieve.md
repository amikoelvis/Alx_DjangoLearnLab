from bookshelf.models import Book
b = Book.objects.get(id=book.id)
b # Expected: <Book: 1984 by George Orwell (1949)>
Book.objects.values().get(id=b.id)

# Expected: {'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}
