from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
import datetime
from exercises.models import Book, Author, Classification, Publisher
from exercises.forms import BookForm, PublisherForm, RegistrationForm

# Create your views here.
# @login_required
# def my_view(request):
#     username = request.POST["username"]
#     password = request.POST["password"]
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             # check if user is an admin
#             if request.user.is_superuser:
#                 login(request, user)
#                 # Redirect to success page 
#                 return HttpResponseRedirect("/create-book/")
#             else:
#                 return HttpResponseRedirect("/books/")
#         else:
#             # Return a 'disabled account' error message
#             return render(request, "invalid_login.html")
#     else:
#         # Return an 'invalid login' error message
#         return render(request, "invalid_login.html")
		
# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect("/")
#     # Redirect to a success page

def is_admin(user):
    return user.is_superuser

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username,email,password)
            
            return render(request, "home.html")
    
    else:
        form = RegistrationForm()
        
    return render(request, "register.html", {"form": form})

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

@login_required
def author_info(request, author_id):
    author = Author.objects.get(id = int(author_id))
    books = Book.objects.filter(author_id = int(author_id))
    return render(
        request,
        'author_info.html',
        {"author": author, "books": books}
    )
 
@login_required  
def book_info(request, book_id):
    book = Book.objects.get(id = int(book_id))
    return render(
        request,
        'book_info.html',
        {"book": book}
    )

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(
        request,
        "book_list.html",
        {"book_list": books}
    )

@login_required
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
    
def search_publisher_form(request):
    return render(request, "search_publisher.html")

def search_publisher(request):
    errors = []
    if "q" in request.GET:
        q = request.GET["q"]
        if not q:
            errors.append("Enter a search term.")
        elif len(q) > 20:
            errors.append("Please enter at most 20 characters")
    else:
        publishers = Publisher.objects.filter(name__icontains=q)
        return render(
            request,
            "search_results_publisher.html",
            {"publisher": publishers, "query": q},
        )
    return render(request, "search_publisher.html", {"errors": errors})

def search_author_form(request):
    return render(request, "search_author.html")

def search_author(request):
    errors = []
    if "q" in request.GET:
        q = request.GET["q"]
        if not q:
            errors.append("Enter a search term.")
        elif len(q) > 20:
            errors.append("Please enter at most 20 characters")
    else:
        authors = Author.objects.filter(first_name__icontains=q)
        return render(
            request,
            "search_results_author.html",
            {"author": authors, "query": q},
        )
    return render(request, "search_author.html", {"errors": errors})

@user_passes_test(is_admin)
def create_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/books/")
    context = {"form": form}
    return render(request, "create_book.html", context)

@user_passes_test(is_admin)
def update_book(request, pk=None):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/books/")
    context = {"form": form}
    return render(request, "update_book.html", context)

@user_passes_test(is_admin)
def delete_book(request, pk=None):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return HttpResponseRedirect("/books/")
    context = {}
    return render(request, "delete_book.html", context)

@user_passes_test(is_admin)
def create_publisher(request):
    form = PublisherForm()
    if request.method == "POST":
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/publishers/")
    context = {"form": form}
    return render(request, "create_publisher.html", context)

@user_passes_test(is_admin)
def update_publisher(request, pk=None):
    publisher = get_object_or_404(Book, pk=pk)
    form = PublisherForm(instance=publisher)
    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/publishers/")
    context = {"form": form}
    return render(request, "update_publisher.html", context)

@user_passes_test(is_admin)
def delete_publisher(request, pk=None):
    publisher = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        publisher.delete()
        return HttpResponseRedirect("/publishers/")
    context = {}
    return render(request, "delete_publisher.html", context)