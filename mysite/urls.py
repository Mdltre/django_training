"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from exercises.views import BookListView, BookDetailView, CreateBookView, UpdateBookView, DeleteBookView, PublisherListView, CreatePublisherView, UpdatePublisherView, DeletePublisherView, SearchAuthorView, SearchPublisherView, SearchHistoryView, hello, current_datetime, calculator, is_valid_date, author_info, book_info, book_list, author_list, classification_info, classification_list, publisher_list, search_publisher_form, search_publisher, search_author_form, search_author, create_book, update_book, delete_book, create_publisher, update_publisher, delete_publisher, create_author, update_author, delete_author, register, logout_view

urlpatterns = [
    #ito lng sir?
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")), 
    

    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout_view'),
    path("math/<int:num1>/<int:num2>/<int:num3>", calculator),
    path("valid-date/<int:year>/<int:month>/<int:day>/", is_valid_date),
    path("hello/", hello),
    path("time/", current_datetime),
    # path("books/", book_list, name='books'),
    path("books/", BookListView.as_view(), name='books'),
    # path("books/<int:book_id>", book_info, name='book-information'),
    path("books/<int:book_id>", BookDetailView.as_view(), name='book-information'),
    path("author/<int:author_id>", author_info, name='author-information'),
    path("classification/", classification_list, name='classification-list'),
    path("classification/<int:classification_id>", classification_info, name='classification'),
    
    # path("publisher/", publisher_list, name='publishers'),
    path("publisher/", PublisherListView.as_view(), name='publishers'),
    # path("publisher/search-form/", search_publisher_form, name="search-publisher"),
    # path("publisher/search/", search_publisher, name="publisher-results"),
    path("publisher/search/", SearchPublisherView.as_view(), name='search-publisher'),
    path("author/", author_list, name='authors'),
    # path("author/search-form/", search_author_form, name="search-author"),
    # path("author/search/", search_author, name="author-results"),
    path("author/search/", SearchAuthorView.as_view(), name='search-author'),
    path("search-history/", SearchHistoryView.as_view(), name='search-history'),
    
    # path("create-book/", create_book),
    path("create-book/", CreateBookView.as_view()),
    # path("<int:pk>/update-book/", update_book),
    path("<int:pk>/update-book/", UpdateBookView.as_view()),
    # path("<int:pk>/delete-book/", delete_book),
    path("<int:pk>/delete-book/", DeleteBookView.as_view()),
    
    # path("create-publisher/", create_publisher),
    path("create-publisher/", CreatePublisherView.as_view()),
    # path("<int:pk>/update-publisher/", update_publisher),
    path("<int:pk>/update-publisher/", UpdatePublisherView.as_view()),
    # path("<int:pk>/delete-publisher/", delete_publisher),
    path("<int:pk>/delete-publisher/", DeletePublisherView.as_view()),
    
    path("create-author/", create_author, name='create-author'),
    path("<int:pk>/update-author/", update_author, name='update-author'),
    path("<int:pk>/delete-author/", delete_author, name='delete-author'),
    
    
]
