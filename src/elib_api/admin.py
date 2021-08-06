from django.contrib import admin
from .models import Author, Category, Book
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ("category",)


class AuthorAdmin(admin.ModelAdmin):
    #exclude = ('pen_name',)
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Book, BookAdmin)
