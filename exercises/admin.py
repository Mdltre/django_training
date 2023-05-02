from django.contrib import admin
from exercises.models import (
    Book,
    Author,
    Classification
)

class BookInline(admin.TabularInline):
    model = Book
    extra = 3
    
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title", "author", "publisher"]})
    ]
    
class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title", "author", "publisher"]})
    ]
    search_fields=["first_name", "last_name"]
    
class PublisherAdmin(admin.ModelAdmin):
    inlines = [BookInline]   
    
admin.site.register(Author)
admin.site.register(Book,BookAdmin)
admin.site.register(Classification)
