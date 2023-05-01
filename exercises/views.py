from django.http import HttpResponse
from django.shortcuts import render
import datetime
from exercises.models import Book, Author, Classification

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def calculator(request, num1, num2, num3=None):
    
    params = [int(num1), int(num2)]
    if num3:
        params.append(int(num3))
    else:
        params.append(0)
        
    final_sum = sum(params)
    difference = params[0] - params[1] - params[2]
    product = params[0] * params[1] * params[2]
    quotient = params[0] / params[1]
    
    return render(
        request,
        "calculator.html",
        {"number1": num1, "number2": num2, "number3": num3, "sum": final_sum, "difference": difference, "product": product, "quotient": quotient}
    )
    
def is_valid_date(request, year, month, day):
    
    is_valid = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        is_valid = False
        
    if(is_valid):
        answer = "The date is valid."
    else:
        answer = "The date is not valid."
        
    return render(
        request,
        "is_valid_date.html",
        {"year": year, "month": month,"day": day, "is_valid": answer}
    )
    
def author_info(request, author_id):
    author = Author.objects.get(id = int(author_id))
    books = Book.objects.filter(author_id = int(author_id))
    return render(
        request,
        'author_info.html',
        {"author": author, "books": books}
    )
    
def book_info(request, book_id):
    book = Book.objects.get(id = int(book_id))
    return render(
        request,
        'book_info.html',
        {"book": book}
    )
    
def book_list(request):
    books = Book.objects.all()
    return render(
        request,
        "book_list.html",
        {"book_list": books}
    )
    
def classification_info(request, classification_id):
    books = Book.objects.filter(classification_id = int(classification_id))
    return render(
        request,
        'classification_info.html',
        {"books": books}
    )
    
def classification_list(request):
    classifications = Classification.objects.all()
    return render(
        request,
        'classification_list.html',
        {"classifications": classifications}
    )