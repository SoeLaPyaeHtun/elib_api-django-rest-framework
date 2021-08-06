from django.contrib import admin
from .models import Author, Category, Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ("category",)


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book,BookAdmin)
