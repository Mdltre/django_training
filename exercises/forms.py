from django.forms import ModelForm
from exercises.models import Book, Publisher, Author, Classification

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        
class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"
        