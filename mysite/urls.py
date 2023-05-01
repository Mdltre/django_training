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
from django.urls import path

from exercises.views import hello, current_datetime, calculator, is_valid_date, author_info, book_info, book_list, classification_info, classification_list

urlpatterns = [
    path("hello/", hello),
    path("time/", current_datetime),
    path("admin/", admin.site.urls),
    path("math/<int:num1>/<int:num2>/<int:num3>", calculator),
    path("valid-date/<int:year>/<int:month>/<int:day>/", is_valid_date),
    
    path("books/", book_list),
    path("books/<int:book_id>", book_info, name='book-information'),
    path("author/<int:author_id>", author_info, name='author-info'),
    path("classification/", classification_list),
    path("classification/<int:classification_id>", classification_info, name='classification'),
]
