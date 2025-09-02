from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books
from .views import LibraryDetailView
from .views import views

urlpatterns = [
    path("books/", list_books, name="list_books"),  # Function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # Class-based view

    # Authentication views
    path("register/", views.register, name="register"),
    path("login/", views.login, LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", views.logout, LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
