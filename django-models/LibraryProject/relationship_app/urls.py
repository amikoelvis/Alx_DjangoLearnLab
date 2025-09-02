from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import LibraryDetailView
from .views import views
from .views import (
    list_books, admin_view, librarian_view, member_view,
)

urlpatterns = [
    path("books/", list_books, name="list_books"),  # Function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # Class-based view

    # Authentication views
    path("register/", views.register, name="register"),
    path("login/", views.login, LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", views.logout, LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),

    # Role-based access control
    path("admin-view/", admin_view, name="admin_view"),
    path("librarian-view/", librarian_view, name="librarian_view"),
    path("member-view/", member_view, name="member_view"),

    path("books/add/", views.add_book, name="add_book"),      # ✅ add_book
    path("books/<int:pk>/edit/", views.edit_book, name="edit_book"),  # ✅ edit_book
    path("books/<int:pk>/delete/", views.delete_book, name="delete_book"),
]
