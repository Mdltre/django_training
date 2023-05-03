from django.forms import ModelForm
from django import forms
from exercises.models import Book, Publisher, Author, Classification

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        
class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"
        
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
       
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length =100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())