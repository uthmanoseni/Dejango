from django.contrib import admin

# Register your models here.
from .models import Author, Book 


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate')
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'isbn')
    search_fields = ('title', 'author__name', 'isbn')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'

