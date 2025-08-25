from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ("title", "author", "publication_year")

    # Add filters (right-hand sidebar in admin)
    list_filter = ("publication_year", "author")

    # Add search capability (search box at the top)
    search_fields = ("title", "author")
