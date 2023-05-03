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
from exercises.views import hello, current_datetime, calculator, is_valid_date, author_info, book_info, book_list, classification_info, classification_list, search_publisher_form, search_publisher, search_author_form, search_author, create_book, update_book, delete_book, create_publisher, update_publisher, delete_publisher, register

urlpatterns = [
    path("hello/", hello),
    path("time/", current_datetime),
    path("admin/", admin.site.urls),
    path("math/<int:num1>/<int:num2>/<int:num3>", calculator),
    path("valid-date/<int:year>/<int:month>/<int:day>/", is_valid_date),
    
    path("books/", book_list),
    path("books/<int:book_id>", book_info, name='book-information'),
    path("author/<int:author_id>", author_info, name='author-information'),
    path("classification/", classification_list),
    path("classification/<int:classification_id>", classification_info, name='classification'),
    
    path("publisher/search-form/", search_publisher_form),
    path("publisher/search/", search_publisher),
    path("author/search-form/", search_author_form),
    path("author/search/", search_author),
    
    path("create-book/", create_book),
    path("<int:pk>/update-book/", update_book),
    path("<int:pk>/delete-book/", delete_book),
    
    path("create-publisher/", create_publisher),
    path("<int:pk>/update-publisher/", update_publisher),
    path("<int:pk>/delete-publisher/", delete_publisher),
    
    # path("login/", my_view),
    path("accounts/", include("django.contrib.auth.urls")), 
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('register/', register, name='register'),
]
