from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import datetime
from exercises.models import Book, Author, Classification, Publisher, MyUser
from exercises.forms import BookForm, PublisherForm, RegistrationForm, AuthorForm

# Create your views here.
#
		
def logout_view(request):
    logout(request)
    return render(request, "logged_out.html")
    # Redirect to a success page

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
def author_list(request):
    authors = Author.objects.all()
    return render(
        request,
        "author_list.html",
        {"author_list": authors}
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

def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(
        request,
        "publisher_list.html",
        {"publisher_list": publishers}
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
            
        authors = Author.objects.filter(first_name__icontains=q)
        return render(
            request,
            "search_results_author.html",
            {"authors": authors, "query": q},
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
            return HttpResponseRedirect("/publisher/")
    context = {"form": form}
    return render(request, "create_publisher.html", context)

@user_passes_test(is_admin)
def update_publisher(request, pk=None):
    publisher = get_object_or_404(Publisher, pk=pk)
    form = PublisherForm(instance=publisher)
    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/publisher/")
    context = {"form": form}
    return render(request, "update_publisher.html", context)

@user_passes_test(is_admin)
def delete_publisher(request, pk=None):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == "POST":
        publisher.delete()
        return HttpResponseRedirect("/publisher/")
    context = {}
    return render(request, "delete_publisher.html", context)

@user_passes_test(is_admin)
def create_author(request):
    form = AuthorForm()
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/author/")
    context = {"form": form}
    return render(request, "create_author.html", context)

@user_passes_test(is_admin)
def update_author(request, pk=None):
    author = get_object_or_404(Author, pk=pk)
    form = AuthorForm(instance=author)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/author/")
    context = {"form": form}
    return render(request, "update_author.html", context)

@user_passes_test(is_admin)
def delete_author(request, pk=None):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        author.delete()
        return HttpResponseRedirect("/author/")
    context = {}
    return render(request, "delete_author.html", context)

class SearchAuthorView(ListView):
    model = Author
    template_name = "search_author.html"
    context_object_name = "authors"
    
    def get_queryset(self):
        query = self.request.GET.get("query")
        if query:
            if not self.request.session["search_history"]:
                self.request.session["search_history"] = [query]
            else:
                self.request.session["search_history"] = self.request.session["search_history"] + [query]
            return Author.objects.filter(first_name__contains=query)
    
        
class SearchPublisherView(ListView):
    model = Publisher
    template_name = "search_publisher.html"
    context_object_name = "publishers"
    
    def get_queryset(self):
        query = self.request.GET.get("query")
        if query:
            return Publisher.objects.filter(name__contains=query)

class BookListView(ListView):
    model = Book
    queryset = Book.objects.all()
    context_object_name = "book_list"
    template_name = "book_list.html"
    
    
class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name="book_info.html"
    
    def get_object(self):
        return get_object_or_404(Book, pk=self.kwargs.get("book_id"))
    
class CreateBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name="create_book.html"
    success_url="/books/"
    
class UpdateBookView(UpdateView):
    model = Book
    form_class = BookForm
    context_object_name = "book"
    template_name = "update_book.html"
    success_url = "/books/"
    
    def get_object(self):
        return get_object_or_404(Book, pk=self.kwargs.get("pk"))
    
class DeleteBookView(DeleteView):
    model = Book
    template_name = "delete_book.html"
    success_url = "/books/"
    
class PublisherListView(ListView):
    model = Publisher
    queryset = Publisher.objects.all()
    context_object_name = "publisher_list"
    template_name = "publisher_list.html"
    
# class PublisherDetailView(DetailView):
#     model = Publisher
#     context_object_name = "publisher"
#     template_name="publisher_info.html"
    
#     def get_object(self):
#         return get_object_or_404(Publisher, pk=self.kwargs.get("publisher_id"))
# wala pla akong publisher details view 

class CreatePublisherView(CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name="create_publisher.html"
    success_url="/publishers/"
    
class UpdatePublisherView(UpdateView):
    model = Publisher
    form_class = PublisherForm
    context_object_name = "publisher"
    template_name = "update_publisher.html"
    success_url = "/publishers/"
    
    def get_object(self):
        return get_object_or_404(Publisher, pk=self.kwargs.get("pk"))
    
class DeletePublisherView(DeleteView):
    model = Publisher
    template_name = "delete_publisher.html"
    success_url = "/publishers/"
    
    

    
